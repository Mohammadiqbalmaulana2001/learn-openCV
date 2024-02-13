import cv2
import numpy as np

image1 = cv2.imread('assets/image1.jpg')
image2 = cv2.imread('assets/image2.jpg')

image3 = cv2.addWeighted(image1,0.5, image2,0.5, 0)

cv2.imshow('image3', image3)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()