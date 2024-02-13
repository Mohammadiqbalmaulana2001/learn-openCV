import cv2

image1= cv2.imread('assets/star.jpg')
image2= cv2.imread('assets/dot.jpg')

sub = cv2.subtract(image1, image2)

cv2.imshow('sub', sub)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()