# cv2.cvtColor() adalah fungsi yang digunakan dalam OpenCV (cv2) untuk mengubah ruang warna (color space) dari suatu gambar. Pada dasarnya, gambar digital dapat direpresentasikan dalam berbagai ruang warna, seperti RGB (Red, Green, Blue), HSV (Hue, Saturation, Value), Grayscale, dan lain-lain. Fungsi cv2.cvtColor() memungkinkan Anda untuk mengonversi gambar dari satu ruang warna ke ruang warna lainnya sesuai kebutuhan aplikasi Anda. Berikut adalah penjelasan singkat tentang cv2.cvtColor():

# cv2.cvtColor(src, code[, dst[, dstCn]]) -> dst

# src: Parameter wajib yang merupakan gambar asli (source) yang ingin Anda ubah ruang warnanya.
# code: Parameter wajib yang menentukan jenis konversi warna yang ingin Anda lakukan. Nilainya harus salah satu dari konstanta warna yang disediakan oleh OpenCV, misalnya cv2.COLOR_BGR2GRAY untuk mengonversi dari ruang warna BGR ke Grayscale, atau cv2.COLOR_BGR2HSV untuk mengonversi dari ruang warna BGR ke HSV.
# dst: Parameter opsional yang merupakan gambar output (destination) untuk menyimpan hasil konversi. Jika tidak disediakan, gambar hasil akan dikembalikan oleh fungsi.
# dstCn: Parameter opsional yang menentukan jumlah saluran (channel) dalam gambar hasil (hanya relevan jika Anda mengonversi ke ruang warna yang memiliki jumlah saluran yang berbeda). Jika tidak disediakan, jumlah saluran akan sama dengan gambar asli.

import cv2

image = cv2.imread(r'road.jpg')
image = cv2.resize(image, (780, 540))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('original', image)
cv2.imshow('gray', gray)

cv2.waitKey(0)