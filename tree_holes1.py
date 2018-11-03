import cv2
import numpy as np

count = 0
img = cv2.imread('./4.jpg', 0)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
blur = cv2.blur(img, (1, 2))

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, param1=50, param2=50,
                           dp=1.3, minDist=5, minRadius=10, maxRadius=23)
circles = np.uint16(np.around(circles))

color_img = cv2.imread("./4.jpg")
red = (0, 0, 255)
for x, y, r in circles[0]:
    cv2.circle(color_img, (x, y), r, red, 2)
    count += 1


cv2.imshow(f'Holes in tree: {count}', color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
