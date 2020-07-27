import numpy as np
import cv2 as cv

vs = cv.VideoCapture(0)

mtx, dist, rvecs, tvecs = (
    np.load("camera_matrix.npy"),
    np.load("distortion_coeff.npy"),
    np.load("rvecs.npy"),
    np.load("tvecs.npy"),
)

angleToWidth = np.degrees(np.math.atan2(13, 17))
print(angleToWidth)

while True:
    success, img = vs.read()
    h, w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    x, y, w, h = roi
    dst = dst[y : y + h, x : x + w]
    centerX, centerY = int(w / 2), int(h / 2)
    print(centerX, centerY)
    dst = cv.line(dst, (0, centerY), (w, centerY), (255, 0, 0), 2)
    dst = cv.circle(dst, (centerX, centerY), 1, (0, 255, 0), 1)
    angleToWidthRatio = (w / 2) / angleToWidth
    for i in range(5, int(angleToWidth), 5):
        dst = cv.circle(
            dst, (int(centerX - angleToWidthRatio * i), centerY), 1, (0, 0, 255), 2
        )
        dst = cv.circle(
            dst, (int(centerX + angleToWidthRatio * i), centerY), 1, (0, 0, 255), 2
        )
    cv.imshow("dst", dst)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cv.destroyAllWindows()
