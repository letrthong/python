#!/usr/bin/env python2.7
from optparse import OptionParser
from itertools import izip_longest
import wave, struct, sys, array
import time

# https://docs.python.org/3/library/wave.html

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def fmtbin(value, sample_width):
    """Format binary value to two-complement format"""
    if sample_width > 1:
        # This would convert the value to unsigned int 
        # but we want a two-complement format
        # value += 2**(8*sample_width) / 2
        if value < 0:
            fvalue = bin(value & (
                    2**(sample_width*8)-1))[2:].zfill(sample_width*8)
        else:
            fvalue = format(value, '#0%ib' % (sample_width*8+2))[2:]
    else:
        fvalue = format(value, '#0%ib' % (sample_width*8+2))[2:]
    # Now add a space after each 4 values
    fvalue = ' '.join(fvalue[i:i+4] for i in xrange(
            0, len(fvalue), 4))
    return fvalue

if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog <Wav-File>")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        print "Missing Wave File"
        parser.print_usage()
        sys.exit(1)
    
    filename = sys.argv[1]

    stream = wave.open(filename,"rb")

    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()
    
    print("num_channels %d", num_channels)
    print("sample_rate %d", sample_rate)
    print("sample_width %d", sample_width)
    print("num_frames %d", num_frames)

    raw_data = stream.readframes(num_frames) # Returns byte data
    stream.close()

    total_samples = num_frames * num_channels

    time.sleep(4)

    if sample_width == 1: 
        fmt = "%iB" % total_samples # read unsigned chars
        integer_data = struct.unpack(fmt, raw_data)
    elif sample_width == 2:
        fmt = "%ih" % total_samples # read signed 2 byte shorts
        integer_data = struct.unpack(fmt, raw_data)
    elif sample_width == 3:
        integer_data = []
        b = array.array('B', raw_data)
        for i in xrange(0, len(b), 3):
            unsigned_value = (b[i] | b[i+1] << 8 | b[i+2] << 16)
            if unsigned_value >> 23:
                value = unsigned_value - (2**24)
            else:
                value = unsigned_value
            integer_data.append(value)
    elif sample_width == 4:
        fmt = "%ii" % total_samples # read signed 2 byte shorts
        integer_data = struct.unpack(fmt, raw_data)
    else:
        raise ValueError("Only supports 8, 16, 24 and 32 bit audio formats.")

    if num_channels == 2:
        for i, (value_left, value_right) in enumerate(grouper(2, integer_data)):
            print "Sample%8i: left: %11i | %s | right: %11i | %s |" % (
                i+1, 
                int(value_left), 
                fmtbin(value_left, sample_width),
                int(value_right),
                fmtbin(value_right, sample_width))
    else:
        for i, data in enumerate(integer_data):
            print "Sample%10i: %11i | %s" % (i+1, int(data), 
                                             fmtbin(data, sample_width))

