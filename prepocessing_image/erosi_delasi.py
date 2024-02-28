# Operasi erosi (erosion) dan dilasi (dilation) adalah dua operasi dasar dalam pemrosesan citra morfologi yang tersedia di OpenCV (cv2). Kedua operasi ini sering digunakan untuk memanipulasi bentuk dan struktur objek dalam gambar. Berikut adalah penjelasan singkat tentang keduanya:

# 1.Erosi (Erosion):

# Operasi erosi digunakan untuk mengurangi ukuran atau mempersempit objek dalam gambar.
# Cara kerjanya adalah dengan menggeser kernel di seluruh gambar dan menghitung nilai minimum piksel yang tertutupi oleh kernel.
# Hasilnya adalah penurunan ukuran objek atau pembersihan noise yang kecil.
# Erosi berguna dalam menghilangkan detail kecil dan memisahkan objek yang saling berdekatan.

# 2.Dilasi (Dilation):

# Operasi dilasi digunakan untuk memperluas ukuran atau melebarkan objek dalam gambar.
# Cara kerjanya adalah dengan menggeser kernel di seluruh gambar dan menghitung nilai maksimum piksel yang tertutupi oleh kernel.
# Hasilnya adalah peningkatan ukuran objek atau pengaburan detail kecil.
# Dilasi berguna dalam menghubungkan bagian yang terputus dari objek, mengisi lubang kecil, dan meningkatkan ukuran objek.

import cv2 
import numpy as np

image = cv2.imread(r'road.jpg')
image = cv2.resize(image, (580, 340))

# membuat karnel
kernel = np.ones((5,5),np.uint8)

# melakukan erosi
erosion = cv2.erode(image, kernel, iterations = 1)

# melakukan delasi
dilation = cv2.dilate(image, kernel, iterations = 1)

cv2.imshow('image', image)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()