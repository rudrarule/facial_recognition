import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cap = cv2.VideoCapture(0)  # Use index 0 for the default camera
cap.set(3, 640)  # Adjusting video length
cap.set(4, 480)  # Adjusting video width
imgBackground = cv2.imread('sources/background.png')

# Importing the mode images into a list
folderModePath = 'sources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in modePathList]
print(len(imgModeList))

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)





while True:
    success, img = cap.read()

    if not success:
        print("Failed to capture frame.")
        break

    # Resize the webcam feed to fit the specified region on the background
    # Resize the webcam feed to fit the specified region on the background
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # Overlay the webcam feed onto the background
    imgBackground[162:162 + 480, 55:55 + 640] = img

    # Overlay the mode image onto another region of the background
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print("matches", matches)
        #print("faceDis", faceDis)

        matchIndex = np.argmin(faceDis)
        # print("Match Index", matchIndex)

        if matches[matchIndex]:
            # print("Known Face Detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

    cv2.imshow("Face Attendance", img)
    cv2.imshow("webcam", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
