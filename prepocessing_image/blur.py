import numpy as np
import cv2

image = cv2.imread(r'road.jpg')
image = cv2.resize(image, (780, 540))

cv2.imshow("original", image)
cv2.waitKey(0)

# Gausian blur
gausian = cv2.GaussianBlur(image, (21,21), 0)
cv2.imshow("gausian", gausian)
cv2.waitKey(0)

# Median Blur 
median = cv2.medianBlur(image, 21) 
cv2.imshow('Median Blurring', median) 
cv2.waitKey(0) 

# Bilateral Blur 
bilateral = cv2.bilateralFilter(image, 21, 80, 80) 
cv2.imshow('Bilateral Blurring', bilateral) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 