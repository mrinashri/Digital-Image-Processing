path='D:/DIP/sunflower-1627193_1920.jpg'

import cv2
import numpy as npp

# Load the image
img1 = cv2.imread(path)
h, w, c = img1.shape


# Loop for a specified number of frames
for i in range(100):
   # Update the image
   ll = img1[:, :(i % w)]
   rr = img1[:, (i % w):]
  
   img2 = npp.hstack((rr, ll))
      
   # Display the updated image
   cv2.imshow( 'animation',img2)

   # Wait for a specified amount of time
   cv2.waitKey(100)

# Close the window
cv2.destroyAllWindows()