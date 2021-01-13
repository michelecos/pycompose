import cv2

img = cv2.imread("Monti.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Monti", img)
cv2.imshow("Grayed", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
