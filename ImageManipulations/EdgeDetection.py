import cv2

img = cv2.imread("opencv-logo.png")
cv2.imshow("Original Image", img)

edgedetect = cv2.Canny(img, 100, 200)
cv2.imshow("Edged Image", edgedetect)

cv2.waitKey(0)  
cv2.destroyAllWindows()

