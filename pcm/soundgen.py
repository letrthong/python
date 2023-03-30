#!/usr/bin/env python2.7

"""This little frequency generator creates bit-perfect signals, which
other programs may not - many add some distortion to the signal.

Remainderless frequences regarding to 44.100kHz
/2 22050
/4 11025
/6 7350
/8 5512
/32 1378
/64 689

Rl. Frequences regarding to 192kHz
/2 96000
/4 48000
/8 24000
/16 12000

"""

from optparse import OptionParser
from contextlib import closing
import sys, math, wave, struct, random

def addsample(vals, value, nchan):
    if nchan == 1:
        vals.append(value)
    if nchan == 2:
        vals.append(value)
        vals.append(value)
    if nchan == 3:
        vals.append(value)
        vals.append(0)
    if nchan == 4:
        vals.append(0)
        vals.append(value)

def sine(sfreq, nframes, channels, srate):
    """Create sine"""
    ts = 1.0 / srate
    t = 0.0
    n = 0
    freq = float(sfreq)
    vals = []
    while n < nframes:
        addsample(vals, math.sin(2.0*math.pi*freq*t), channels)
        n = n + 1
        t = t + ts
    return vals
    
def square(sfreq, nframes, channels, srate):
    """Create square signal"""
    # Calc amount of samples / period (without remainder)
    spnum = srate / sfreq
    srate_div = 1.0/srate
    freq_div = 1.0/sfreq
    vals = []
    s_period = 0.0
    t = 0
    nsamples = 0
    while nsamples < nframes:
        while s_period < t*freq_div - freq_div/2:
            addsample(vals, 1, channels)
            s_period += srate_div
            nsamples += 1
        while s_period < t*freq_div:
            addsample(vals, -1, channels)
            s_period += srate_div
            nsamples += 1
        t += 1
    return vals
    
def silence(sfreq, nframes, channels, srate):
    """Create zero signal (silence)"""
    vals = []
    for i in range(nframes):
        addsample(vals, 0, channels)
    return vals

def dc(sfreq, nframes, channels, srate):
    """Create positive DC signal"""
    vals = []
    for i in range(nframes):
        addsample(vals, 1, channels)
    return vals

def wnoise(sfreq, nframes, channels, srate):
    """Create white noise (same noise on both channels)"""
    vals = []
    random.seed(None)
    for i in range(nframes):
        addsample(vals, random.randint(-1,1), channels)
    return vals

# FIXME - other signals would be interesting: Ramp, Sawtooth,
# various noise variants (pink noise, brown noise...)
# A Frequency sweep would also be nice
    
if __name__ == '__main__':
    parser = OptionParser(
        usage="usage: %prog [options]")
    parser.add_option("-t", "--stype", dest="stype",
                      default="sine",
                      help="Signal type [sine, square, silence, dc], "
                      "default: sine")
    parser.add_option("-o", "--output-file", dest="ofile",
                      default="sample.wav",
                      help="Name of output file, default: sample.wav")
    parser.add_option("-d", "--duration", dest="duration",
                      type="int", default=15000,
                      help="Sample Duration in milliseconds, default: 15000")
    parser.add_option("-r", "--srate", dest="srate",
                      type="int", default=44100,
                      help="Sampling Rate, default: 44100")
    parser.add_option("-b", "--bdepth", dest="bdepth",
                      type="int", default=16,
                      help="Sampling Bit Depth [8, 16, 24, 32], default: 16")
    parser.add_option("-f", "--sfreq", dest="sfreq",
                      type="int", default=1000,
                      help="Signal (e.g. sine/square) frequency in Hz, "
                      "default: 1000 (= 1kHz)")
    parser.add_option("-l", "--slevel", dest="slevel", default="0dB",
                      help="Signal level, either int (e.g. 32768) or -dB "
                      "(10dB), default: "
                      "0dB (maximum volume)")
    parser.add_option("-c", "--channels", dest="channels",
                      type="int", default=1,
                      help="Number of Channels: 1 = mono, 2 = stereo, "
                      " 3 = left only / right zero, 4 = right only / "
                      "left zero; default: 1")
    parser.add_option("-s", "--sequence", dest="sequence",
                      help="Sequence of patterns, e.g. 10 seconds sine, then "
                      "5 seconds silence etc. The syntax is: "
                      "(type1,frequency1,length1;type2,frequency2,length2;...) "
                      "e.g. (sine,440,1000;silence,0,20,square,880,200)")

    (options, args) = parser.parse_args()
    if len(args) != 0:
        print "Incorrect number of parameters"
        parser.print_usage()
        sys.exit(1)

    if options.bdepth not in (8,16,24,32):
        print
        print "ERROR: Incorrect bit depth!"
        print
        parser.print_help()
        sys.exit(1)
        
    if options.bdepth == 8:
        # unsigned char
        minval = 0
        maxval = 255
    else:
        # signed int
        minval = -2**options.bdepth/2
        maxval = 2**options.bdepth/2-1
        
    # Now eventually correct maxval/minval
    slevel = options.slevel
    minval1 = minval
    maxval1 = maxval
    minval2 = minval
    maxval2 = maxval
    try:
        if slevel.lower().endswith("db"):
            # Level given in dB
            dbval = -int(slevel[:-2])
            factor = 10 ** (dbval / 10.)
            minval1 = int(round(minval * factor))
            maxval1 = int(round(maxval * factor))
        elif slevel.isdigit():
            # Level given as number
            if options.bdepth == 8:
                maxval1 = 255-(127-int(slevel))
                minval1 = 0+(128-int(slevel))
            else:
                minval = -int(slevel)
                maxval = int(slevel)
                
    except ValueError:
        print "Incorrect level syntax!"
        print
        parser.print_help()
        sys.exit(1)

    # Set the new levels accordingly
    if minval1 > minval and minval1 < maxval2:
        minval = minval1
    if maxval1 < maxval and maxval1 > minval2:
        maxval = maxval1

    if options.channels not in (1,2,3,4):
        print 
        print "ERROR: Incorrect number of channels!"
        print
        parser.print_help()
        sys.exit(1)
    else:
        channels = options.channels
        if channels > 1:
            nchan = 2
        else:
            nchan = 1
    
    sampwidth = options.bdepth / 8
    srate = options.srate
                          
    if options.sequence is None:
        # No sequence given, create one-element sequence from default
        # values / given types
        sequence = "%s,%s,%s" % (options.stype,options.sfreq,options.duration)
    else:
        sequence = options.sequence

    vals = []
    # A sequence is given instead of a single type
    # First try to parse the sequence string, split after ";"
    slist = sequence.split(";")
    for pattern in slist:
        try:
            stype, sfreq, duration = pattern.split(",")
            sfreq = int(sfreq)
            duration = int(duration)
        except ValueError:
            print slist
            print
            print "ERROR: Incorrect sequence syntax!"
            print
            #parser.print_help()
            sys.exit(1)
        nframes = int(duration * srate / 1000.0)
        if stype == "sine":
            print "Adding sine, %sHz for %sms" % (sfreq, duration)
            vals.extend(sine(sfreq, nframes, channels, srate))
        elif stype == "square":
            print "Adding square, %sHz for %sms" % (sfreq, duration)
            vals.extend(square(sfreq, nframes, channels, srate))
        elif stype == "silence":
            print "Adding silence for %s ms" % duration
            vals.extend(silence(sfreq, nframes, channels, srate))
        elif stype == "dc":
            print "Adding dc for %s ms" % duration
            vals.extend(dc(sfreq, nframes, channels, srate))
        elif stype == "wnoise":
            print "Adding white noise for %s ms" % duration
            vals.extend(wnoise(sfreq, nframes, channels, srate))
        else:
            print
            print "ERROR: Incorrect signal type!"
            print
            parser.print_help()
            sys.exit(1)

    # FIXME - The volume should also be made available in sequence

    qvals = []

    if options.bdepth > 8:
        for val in vals:
            if val >= 0:
                qvals.append(min(maxval, (int) (val * float(abs(minval)))))
            else:
                qvals.append(max(minval, (int) (val * float(abs(minval)))))
    else:
        for val in vals:
            if val >= 0:
                qvals.append(min(maxval, 128+(int) (val * float(
                                    abs(maxval/2)))))
            else:
                qvals.append(max(minval, 128+((int) (val * float(
                                    abs(maxval/2))))))

    # Format data in wave-compatible string (struct)
    tdata = []
    if options.bdepth == 8:
        for qval in qvals:
            tdata.append(struct.pack("<B", qval))
    elif options.bdepth == 16:
        for qval in qvals:
            tdata.append(struct.pack("<h", qval))
    elif options.bdepth == 24:
        for qval in qvals:
            tdata.append(struct.pack('BBB', 
                                      (qval & 0x0000ff),
                                      (qval & 0x00ff00) >> 8,
                                    (qval & 0xff0000) >> 16))
    elif options.bdepth == 32:
        for qval in qvals:
            tdata.append(struct.pack("<i", qval))
    else:
        print
        print "ERROR: Incorrect bit depth!"
        print
        parser.print_help()
        sys.exit(1)

    # Now write wave file
    wout = wave.open(options.ofile, "wb")
    comptype = "NONE"
    compname = "no compression"
    wout.setparams((nchan, sampwidth, srate, nframes, 
                    comptype, compname))
    wout.writeframes(''.join(tdata))
    wout.close()
