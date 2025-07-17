#Method 01
import cv2
 
# Load the image
img = cv2.imread('D:/DIP/sunflower-1627193_1920.jpg')
 
# Invert the image using cv2.bitwise_not
img_neg = cv2.bitwise_not(img)
 
# Show the image
cv2.imshow('negative',img_neg)
cv2.waitKey(0)


#Method 02
# Load the image
img = cv2.imread('D:/DIP/sunflower-1627193_1920.jpg', cv2.COLOR_BGR2RGB)

height, width, _ = img.shape
  
for i in range(0, height - 1):
   for j in range(0, width - 1):
      # each pixel has RGB channle data 
      pixel = img[i, j]
      
      # red
      pixel[0] = 255 - pixel[0]
      
      # green
      pixel[1] = 255 - pixel[1]
      
      # blue
      pixel[2] = 255 - pixel[2]
      
      # Store new values in the pixel
      img[i, j] = pixel
        
# Display the negative transformed image
cv2.imshow('negative image1', img)
cv2.waitKey(0)


#Method 03
import cv2

img = cv2.imread('D:/DIP/sunflower-1627193_1920.jpg')

# Subtract the img array values from max value(calculated from dtype)
img_neg = 255 - img

# Show the negative image
cv2.imshow('negative',img_neg)
cv2.waitKey(0)


#Negative Transform for Grayscale image
import cv2
 
# Load the image
gray = cv2.imread('D:/DIP/img_grayscale.jpg', 0)
 
cv2.imshow('Gray image:', gray)

# Invert the image using cv2.bitwise_not
gray_neg = cv2.bitwise_not(gray)
 
# Show the image
cv2.imshow('negative',gray_neg)
cv2.waitKey(0)
