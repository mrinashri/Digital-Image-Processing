import cv2

img = cv2.imread('D:/DIP/pexels6.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv = 255 - gray
blur = cv2.GaussianBlur(inv, (21, 21), 0)
sketch = cv2.divide(gray, 255 - blur, scale=256)

cv2.imshow("Original", img)
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
