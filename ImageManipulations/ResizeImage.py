import cv2

img = cv2.imread("opencv-logo.png")
cv2.imshow("Original Image", img)

newImg = cv2.resize(img, (200, 200))
cv2.imshow("Resized Image", newImg)

cv2.waitKey(0)  
cv2.destroyAllWindows()

