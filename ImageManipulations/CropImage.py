import cv2

img = cv2.imread("opencv-logo.png")
cv2.imshow("Original Image", img)

height, width = img.shape[0:2]

startRow = int(height * 0.15)
startCol = int(width * 0.15)

endRow = int(height * 0.85)
endCol = int(width * 0.85)

croppedImage = img[startRow:endRow, startCol:endCol]
cv2.imshow("Cropped Image", croppedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()