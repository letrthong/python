import qrcode

from PIL import Image

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
img.save("qrcode_overlay.jpg")

print(f"The QR code from {data} is successfully saved to qrcode.jpg file.")


# Open the background image
background = Image.open("test.jpg")

# Open the overlay image
overlay = Image.open("qrcode_overlay.jpg").convert("RGBA")

# Resize the overlay image
overlay_size = (100, 100)  # Set the desired size (width, height)
overlay = overlay.resize(overlay_size, Image.ANTIALIAS)

# Calculate position (top-left corner)
position = (50, 50)

# Create a mask using the alpha channel of the overlay
mask = overlay.split()[3]

# Paste the overlay image on the background image using the mask
background.paste(overlay, position, mask)

# Save the result
background.save("result.jpg")
