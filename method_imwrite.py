import cv2

image = cv2.imread('assets/road.jpg')

cv2.imwrite('assets/ouput.jpg', image)

print('Gambar berhasil di simpan')