import cv2
import face_recognition

known_image = face_recognition.load_image_file("faces/user.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    rgb = frame[:, :, ::-1]

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding in encodings:

        match = face_recognition.compare_faces(
            [known_encoding],
            encoding
        )

        if True in match:
            print("Access Granted")
            video.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Face Login", frame)

    if cv2.waitKey(1) == 27:
        break