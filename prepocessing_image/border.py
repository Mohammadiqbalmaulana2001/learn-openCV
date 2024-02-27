import cv2

image = cv2.imread(r'road.jpg')
image= cv2.resize(image, (780, 250))

border = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = [252, 235, 25])
border1= cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)


cv2.imshow('border', border)
cv2.waitKey(0)

cv2.imshow('border1', border1)
cv2.waitKey(0)