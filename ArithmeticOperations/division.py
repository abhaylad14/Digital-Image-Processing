import cv2

img1 = cv2.imread('ml.png')

div = img1 / img1
cv2.imshow("Addition", div)
cv2.waitKey(0)
cv2.destroyAllWindows()