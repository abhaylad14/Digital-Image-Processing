import cv2

img1 = cv2.imread('ml.png')

add = img1 + img1
cv2.imshow("Addition", add)
cv2.waitKey(0)
cv2.destroyAllWindows()