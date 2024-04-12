import cv2

# Read an image
image = cv2.imread('image/Cat03.jpg')

# Retrieve pixel value at coordinates (x, y)
x, y = 50, 50
pixel_value = image[y, x]
print(f"Pixel value at ({x},{y}): R={pixel_value[2]}, G={pixel_value[1]}, B={pixel_value[0]}")

# Draw a green circle at coordinates (x, y)
cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

# Display the image
cv2.imshow('Image with Circle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
