import qrcode

# Data to be encoded
data = "https://copilot.microsoft.com"

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save the QR code as "qrcode.jpg"
img.save("qrcode.jpg")

print(f"The QR code from {data} is successfully saved to qrcode.jpg file.")
