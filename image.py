# 
# pip install pillow
#

from PIL import Image

# Open the background image
background = Image.open("background.jpg")

# Open the overlay image
overlay = Image.open("overlay.jpg").convert("RGBA")

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
