import cv2
import numpy as np

img = cv2.imread("ml.png")
cv2.imshow("Original Image", img)

kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilated Image", img_dilation)

cv2.waitKey(0)  
cv2.destroyAllWindows()
