import numpy as np
import cv2 

image = cv2.imread(r'road.jpg')

window_name = "image"

kernel = np.ones((6,6),np.uint8)

image = cv2.resize(image, (780, 540))
images = cv2.erode(image,kernel, cv2.BORDER_REFLECT)

cv2.imshow(window_name, images)

cv2.waitKey(0)