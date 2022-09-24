 
from escpos.printer import Usb
 
# BIXOLON SLP-TX403 - BPL-Z
# lsusb
# Bus 001 Device 002: ID 1504:0027 BIXOLON BIXOLON SLP-TX403
# USB vendor and product Ids 


p = Usb(0x1504, 0x0027, 0, profile="BIXOLON BIXOLON SLP-TX403")
p.text("Hello World\n")
#p.image("logo.gif")
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')