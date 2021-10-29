import cv2

img1 = cv2.imread('ml.png')

mul = img1 * img1
cv2.imshow("Multiplication", mul)
cv2.waitKey(0)
cv2.destroyAllWindows()