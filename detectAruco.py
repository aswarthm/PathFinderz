import argparse
from imutils.video import VideoStream
import imutils
import cv2
import sys

image = cv2.imread("10.png")
cap = cv2.VideoCapture("ArucoVid.mp4")
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
arucoParams = cv2.aruco.DetectorParameters_create()

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

for i in range(45):
    cap.set(1, i*10)
    ret, frame = cap.read()
    cv2.waitKey(1)
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    x, y = getCoords(corners[0][0])
    print(x, y)


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