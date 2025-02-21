import cv2
import numpy as np
import os
import glob

# Set image folder path
image_folder = r'C:\Users\spars\PycharmProjects\PythonProject\webcam\images for calibration'
images = glob.glob(os.path.join(image_folder, '*.jpg'))
image_size = None
objp = np.zeros((5*7, 3),np.float32)
objp[:,:2] = np.mgrid[0:7,0:5].T.reshape(-1,2)

objectPoints=[]
imagePoints=[]

# Define the ArUco dictionary and ChArUco board
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
board = cv2.aruco.CharucoBoard((5, 7), 0.04, 0.03, aruco_dict)
aruco_params = cv2.aruco.DetectorParameters()
aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)
charuco_detector = cv2.aruco.CharucoDetector(board)

for img_path in images:
    frame = cv2.imread(img_path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect ArUco markers
    marker_corners, marker_ids,_ = aruco_detector.detectMarkers(gray)
    image_size = gray.shape[::-1]
    # print(marker_corners)
    # print(marker_ids)
    # Detect Charuco
    success,mxt,distort,_=cv2.aruco.calibrateCameraAruco(marker_corners,marker_ids,board=board,imageSize=image_size,cameraMatrix=None,distCoeffs=None)

    if success:
            print("Camera calibration successful!")
            print("Camera matrix:\n", mxt)
            print("Distortion coefficients:\n", distort)
    else:
            print("Calibration failed.")

    # ret, corners,ids = cv2.aruco.interpolateCornersCharuco(marker_corners,marker_ids,gray,board)
    # print(corners.shape)
    #
    # # print(ids)
    # if ret:
    #     objectPoints.append(board.getObjPoints())
    #     imagePoints.append(corners)
    #     objectPoints = np.asarray(objectPoints)
    #     # print(np.asarray(objectPoints).shape)
    #     print(objectPoints.shape)
    #     print(objectPoints[0])
    #         # print("object points are =",objectPoints)
    #             # print(imagePoints)
    #     mtx,dist,_ = cv2.aruco.calibrateCameraCharuco(charucoCorners=objectPoints, charucoIds=marker_ids, board=board, imageSize=gray.shape,cameraMatrix=None, distCoeffs=None)
    # exit("PAused")

