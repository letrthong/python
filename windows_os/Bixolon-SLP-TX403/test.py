import win32print
import win32api

printer_name = "BIXOLON SLP-TX403"
hprinter = win32print.OpenPrinter(printer_name)
win32print.StartDocPrinter(hprinter, 1, ("Test Print", None, "RAW"))
win32print.WritePrinter(hprinter, b"Hello, Bixolon!")
win32print.EndDocPrinter(hprinter)
win32print.ClosePrinter(hprinter)
