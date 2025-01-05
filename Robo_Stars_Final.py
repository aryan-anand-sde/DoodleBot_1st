import cv2
import numpy

image = cv2.imread("A:\CODING\Arduino\Sample 2.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
parameters = cv2.aruco.DetectorParameters()

detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
corners, ids, rejected = detector.detectMarkers(gray)
list_ids = list(ids)

# list_corners = list(corners[0])
list_index = []
turns = ['S']

# print(list_corners[0][1])
for i in range(0, len(list_ids)):
    list_index.append(list_ids.index(i))
# print(list_index)

for i in range(1, len(list_index) - 1):
    list_corners0 = list(corners[list_index[i - 1]])
    list_corners1 = list(corners[list_index[i]])
    list_corners2 = list(corners[list_index[i + 1]])
    if list_corners0[0][0][0] < list_corners1[0][0][0]:
        # if(list_corners2[0][0][1] == list_corners1[0][0][1]):
        #   turns.append('S')
        if list_corners2[0][0][1] > list_corners1[0][0][1]:
            turns.append("R")
        if list_corners2[0][0][1] < list_corners1[0][0][1]:
            turns.append("L")

    elif list_corners0[0][0][0] > list_corners1[0][0][0]:
        # if(list_corners2[0][0][1] == list_corners1[0][0][1]):
        #   turns.append('S')
        if list_corners2[0][0][1] > list_corners1[0][0][1]:
            turns.append("L")
        if list_corners2[0][0][1] < list_corners1[0][0][1]:
            turns.append("R")

    elif list_corners0[0][0][1] < list_corners1[0][0][1]:
        # if(list_corners2[0][0][0] == list_corners1[0][0][0]):
        #   turns.append('S')
        if list_corners2[0][0][0] > list_corners1[0][0][0]:
            turns.append("L")
        if list_corners2[0][0][0] < list_corners1[0][0][0]:
            turns.append("R")

    else:
        if list_corners2[0][0][0] > list_corners1[0][0][0]:
            turns.append("R")
        if list_corners2[0][0][0] < list_corners1[0][0][0]:
            turns.append("L")

turns.append("F")
print(turns)
# if ids is not None:
#     cv2.aruco.drawDetectedMarkers(image, corners, ids)
#     cv2.imshow('Detected Markers', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()