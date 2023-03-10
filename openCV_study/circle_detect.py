import cv2

src = cv2.imread("colorball.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 10, minRadius = 80, maxRadius = 100)

for i in circles[0]:
    # cv2.line(dst, (int(i[0]), int(i[1])), (int(i[0]), int(i[1])), (255, 255, 255), 5)
    # print(i[1]);
    cv2.circle(dst, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 255), 5)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()