import cv2

image_convert = cv2.imread('D:/DIP/pexels6.jpg', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(image_convert, cv2.COLOR_BGR2GRAY)
threshold, img_black = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('pexels6.jpg', img_black)
cv2.imwrite('img_grayscale.jpg', img_gray)
cv2.imwrite('img_black.jpg', img_black)

cv2.waitKey(0)
cv2.destroyAllWindows()