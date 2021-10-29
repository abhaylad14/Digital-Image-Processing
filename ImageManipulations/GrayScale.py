import cv2

img = cv2.imread("opencv-logo.png")
cv2.imshow("Original Image", img)

newImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", newImg)

cv2.waitKey(0)  
cv2.destroyAllWindows()

