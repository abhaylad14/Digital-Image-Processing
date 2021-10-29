import cv2
import numpy as np

img = cv2.imread("opencv-logo.png")
cv2.imshow("Original Image", img)

contrastimg = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
cv2.imshow("Contrast Image", contrastimg)

cv2.waitKey(0)  
cv2.destroyAllWindows()
