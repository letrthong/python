from escpos.printer import Serial
printer = Serial(devfile='COM10', baudrate=9600)
printer.text("Hello, Bixolon SLP-TX403!\n")
printer.cut()