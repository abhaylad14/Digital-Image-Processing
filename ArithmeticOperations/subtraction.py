import cv2

img1 = cv2.imread('ml.png')

sub = img1 - img1
cv2.imshow("Subtraction", sub)
cv2.waitKey(0)
cv2.destroyAllWindows()