import cv2
import numpy as np

img = cv2.cv2.imread('random_image.jpg')
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()