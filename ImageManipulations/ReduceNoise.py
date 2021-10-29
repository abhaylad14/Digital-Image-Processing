import cv2

img = cv2.imread("lena.jpg")
cv2.imshow("Original Image", img)

newImg = cv2.fastNlMeansDenoisingColored(img,None,20,10,7,21)
cv2.imshow("Reduced Noise Image", newImg)

cv2.waitKey(0)  
cv2.destroyAllWindows()

