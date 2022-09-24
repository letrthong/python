 
from escpos.printer  import Usb

import usb.core
import sys
 
import os, sys 

from win32printing import Printer
 

# BIXOLON SLP-TX403 - BPL-Z
# lsusb
# Bus 001 Device 002: ID 1504:0027 BIXOLON BIXOLON SLP-TX403
# USB vendor and product Ids  profile SLP-TX403
 # idVendor 0x1504, idProduct 0x0027

idVendor= 0x1504
idProduct=0x0027 

interface=0
in_ep=0x81 
out_ep=0x02



device = usb.core.find(idVendor=idVendor, idProduct=idProduct)
if device is None:

    print('ADU Device not found. Please ensure it is connected to the tablet.')
    print('win32printing on Windows OS')
    printer_name='BIXOLON SLP-TX403 - BPL-Z'

    font = {
        "height": 8,
    }
 
    with Printer(linegap=1, printer_name=printer_name) as printer:
        printer.text("title1", font_config=font)

    
    sys.exit(1)


epson  = Usb(idVendor, idProduct, interface , in_ep, out_ep)
epson.text("Telua Company \n")
epson.qr("You can readme from your smartphone")
 
epson.cut()
 