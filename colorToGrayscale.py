
import cv2

# Load color image
img = cv2.imread("C:/Users/HP/Downloads/rgbPhoto.jpg")

# Convert color image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_img)
cv2.imwrite('C:/Users/HP/Downloads/grayscalePhoto.jpg',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()