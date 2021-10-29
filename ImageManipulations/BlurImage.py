import cv2
import numpy as np

img = cv2.imread("lena.jpg")
cv2.imshow("Original Image", img)

blurimg = cv2.medianBlur(img, 25)
cv2.imshow("Blur Image", blurimg)

newImg = cv2.cvtColor(blurimg, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", newImg)


cv2.waitKey(0)  
cv2.destroyAllWindows()
