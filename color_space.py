
import cv2 as cv
import numpy as np

# Read the image
frame = cv.imread("images.jpeg")

if frame is None:
    print("Error: Could not load image.")
    exit()

# Convert BGR to HSV
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# Define range for dark gray/black pole
lower_pole = np.array([0, 0, 0])
upper_pole = np.array([180, 255, 100])

# Threshold the HSV image to get dark objects
mask = cv.inRange(hsv, lower_pole, upper_pole)

# Bitwise-AND mask and original image
res = cv.bitwise_and(frame, frame, mask=mask)

# Display the images
cv.imshow("frame", frame)
cv.imshow("mask", mask)
cv.imshow("res", res)

cv.waitKey(0)
cv.destroyAllWindows()
