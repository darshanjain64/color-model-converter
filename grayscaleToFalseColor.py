import cv2
import numpy as np

# Load grayscale image
gray_img = cv2.imread('C:/Users/HP/Downloads/grayscalePhoto.jpg', 0)

# Create a color map using a lookup table (LUT)
color_map = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)

# Display the false color image
cv2.imshow('False Color Image', color_map)
cv2.imwrite('C:/Users/HP/Downloads/falsePhoto.jpg',color_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
