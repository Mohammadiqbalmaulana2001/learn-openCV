import cv2
import numpy as np
import matplotlib.pyplot as plt

# membaca gambar menggunakan cv2
img = cv2.imread('assets/road.jpg', cv2.IMREAD_COLOR)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()


# membaca gambar menggunakan matplotlib
plt.imshow(img)

plt.waitforbuttonpress()

plt.close()

# Mengubah warna BGR ke format warna RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(RGB_img)

plt.waitforbuttonpress()

plt.close('all')

# Membuka dalam mode skala abu-abu
path = r"assets/road.jpg"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

cv2.imshow('image', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()