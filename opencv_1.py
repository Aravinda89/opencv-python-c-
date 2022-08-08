# Read, Display and Write an Image using OpenCV

import cv2

# The function cv2.imread() is used to read an image.
img_path = r'C:\Users\yga\Desktop\test_image.jpg'

img_color = cv2.imread(img_path,1)
img_grayscale = cv2.imread(img_path,0)
img_unchanged = cv2.imread(img_path,-1)

# cv2.IMREAD_UNCHANGED  or -1
# cv2.IMREAD_GRAYSCALE  or 0
# cv2.IMREAD_COLOR  or 1

# The function cv2.imshow() is used to display an image in a window.
#Displays image inside a window
cv2.imshow('color image',img_color)  
cv2.imshow('grayscale image',img_grayscale)
cv2.imshow('unchanged image',img_unchanged)
	 
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()

# The function cv2.imwrite() is used to write an image.
cv2.imwrite(r'C:\Users\yga\Desktop\grayscale1.jpg', img_grayscale)

print('Done')