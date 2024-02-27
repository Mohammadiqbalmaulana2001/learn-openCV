import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'road.jpg')

setengah = cv2.resize(image , (0, 0) , fx = 0.1 , fy= 0.1)
lebih_besar = cv2.resize(image , (1050 , 1610))

stretch_near = cv2.resize(image, (780, 540), 
                interpolation = cv2.INTER_LINEAR)

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]

images = [image ,setengah, lebih_besar,stretch_near]
count = 4

for i in range(4):
    plt.subplot(2 ,2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()