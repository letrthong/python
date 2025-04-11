import cv2
import numpy as np

# Load the image
image = cv2.imread('test.jpg')

# Create a mask with the same dimensions as the image
mask = np.zeros_like(image)

# Define the center and radius of the circle
center = (image.shape[1] // 2, image.shape[0] // 2)
radius = min(center[0], center[1], image.shape[1] - center[0], image.shape[0] - center[1])

# Draw a white filled circle on the mask
cv2.circle(mask, center, radius, (255, 255, 255), -1)

# Apply the mask to the image
circular_cropped_image = cv2.bitwise_and(image, mask)

# Save the result
cv2.imwrite('circular_cropped_image.jpg', circular_cropped_image)
