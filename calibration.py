import numpy as np
import cv2 as cv
import glob
import time

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
images = glob.glob("*.jpg")

vs = cv.VideoCapture(0)

while True:
    success, img = vs.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (9, 6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        cv.drawChessboardCorners(img, (9, 6), corners2, ret)
        if cv.waitKey(33) == ord("a"):
            objpoints.append(objp)
            imgpoints.append(corners)
            print("Saved points")
    cv.imshow("img", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break


ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None
)

np.save("camera_matrix.npy", mtx)
np.save("distortion_coeff.npy", dist)
np.save("rvecs.npy", rvecs)
np.save("tvecs.npy", tvecs)

print(mtx, dist, rvecs, tvecs)

cv.destroyAllWindows()
