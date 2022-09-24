 
from escpos import *
 
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


epson  = printer.Usb(idVendor, idProduct, interface , in_ep, out_ep)

epson.text("Thonng Le Trung \n")
 
#epson.barcode('1324354657687', 'EAN13', 64, 2, '', '')
epson.cut()
 