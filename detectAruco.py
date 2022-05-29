import argparse
from imutils.video import VideoStream
import imutils
import cv2
import sys
import math
import numpy as np

image = cv2.imread("10.png")
cap = cv2.VideoCapture("ArucoVid.mp4")
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
arucoParams = cv2.aruco.DetectorParameters_create()

distCoeffs = [-4.1802327176423804e-001,5.0715244063187526e-001,0.00,0.00,-5.7843597214487474e-001]
cameraMatrix = [[6.5746697944293521e+002,0.00,3.1950000000000000e+002], [0.00,6.5746697944293521e+002,2.3950000000000000e+002], [0.00,0.00,1.00]]

cameraMatrix = np.asarray(cameraMatrix)
distCoeffs = np.asarray(distCoeffs)


i = 1
# frame_seq = i * 10
# while cap.isOpened():
#     frame_no = (frame_seq /(15*30))
#     i += 1
#     cap.set(2,frame_no)
#     ret, frame = cap.read()
#     if ret == True:
#         (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
#         print(corners)
# print(i)

def getCoords(corners):
    x = 0
    y = 0
    for i in corners:
        x += corners[0][0]
        y += corners[0][1]
    x = x/4
    y = y/4
    return (x,y)

def getYPR(R):
    sin_x    = math.sqrt(R[2,0] * R[2,0] +  R[2,1] * R[2,1])    
    z1    = math.atan2(R[2,0], R[2,1])     # around z1-axis
    x      = math.atan2(sin_x,  R[2,2])     # around x-axis
    z2    = math.atan2(R[0,2], -R[1,2])    # around z2-axis
    yawpitchroll_angles = -180*np.array([[z1], [x], [z2]])/math.pi
    yawpitchroll_angles[1,0] = yawpitchroll_angles[1,0]+90

    return np.array([[z1], [x], [z2]])


for i in range(45):
    cap.set(1, i * 10)
    ret, frame = cap.read()
    cv2.waitKey(1)
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    #x, y = getCoords(corners[0][0])
    
    rvec, tvec, f = cv2.aruco.estimatePoseSingleMarkers(corners, 4, cameraMatrix, distCoeffs)
    #print(tvec)
    rmat, jacobian = cv2.Rodrigues(rvec)
    yaw, p, r = getYPR(rmat)
    print(str(i*10) + "={" + str(round(tvec[0][0][0], 4)) + "," + str(round(tvec[0][0][2], 4)) + "," + str(round(tvec[0][0][2], 4)) + "}{" +  str(round(yaw[0], 4)) + "," + str(round(p[0], 4)) + "," + str(round(r[0], 4)) + "}")


# (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
# # #720*462
# print(corners[0][0])
# x = 0
# y = 0
# for i in corners[0][0]:
#     x += i[0]
#     y += i[1]
# x = 720/2 - x/4
# y = 462/2 - y/4

# print(x, y)