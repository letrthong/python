 
from escpos.printer  import Usb

import usb.core
import sys
 
import os, sys 

import win32print

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
    font = {
        "height": 8,
    }

    p = win32print.OpenPrinter ("BIXOLON SLP-TX403 - BPL-Z")

    job = win32print.StartDocPrinter (p, 1, ("test of raw data", None, "RAW")) 
    win32print.StartPagePrinter (p) 
    win32print.WritePrinter (p, "data to print")
    win32print.EndPagePrinter (p)

    sys.exit(1)


epson  = Usb(idVendor, idProduct, interface , in_ep, out_ep)
epson.text("Telua Company \n")
epson.qr("You can readme from your smartphone")
 
epson.cut()
 