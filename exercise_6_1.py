import cv2

image = cv2.imread('image/Cat03.jpg')
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.imwrite('image/output.jpg',image)
