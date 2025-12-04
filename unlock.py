import cv2
import os
import numpy as np
import random
import time
from twilio.rest import Client
from twilio_config import account_sid, auth_token, twilio_number
import RPi.GPIO as GPIO  # import hardware_control

RELAY_PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
# GPIO.output(RELAY_PIN,GPIO.LOW)


def unlock_sequence():
    print("Door Unlocked (Relay ON)")
    GPIO.output(18, 1)
    print("Thank you")


def cleanup_gpio():
    GPIO.cleanup()


recognizer = cv2.face.LBPHFaceRecognizer_create()
faces = []
labels = []
label_to_mobile = {}
dataset_path = "dataset"
label_counter = 0

# Load face data from subfolders
for user_folder in os.listdir(dataset_path):
    user_path = os.path.join(dataset_path, user_folder)
    if os.path.isdir(user_path):
        number_file = os.path.join(user_path, "number.txt")
        if os.path.exists(number_file):
            with open(number_file, "r") as f:
                mobile_number = f.read().strip()
            label_to_mobile[label_counter] = mobile_number

        for img_name in os.listdir(user_path):
            if img_name.endswith(".jpg"):
                img_path = os.path.join(user_path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    faces.append(img)
                    labels.append(label_counter)

        label_counter += 1

if not faces:
    print("? No registered faces found. Please run register_face.py first.")
    cleanup_gpio()
    exit()

recognizer.train(faces, np.array(labels))

# Load Haar cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
if face_cascade.empty():
    print("? Error loading Haar Cascade file.")
    cleanup_gpio()
    exit()

# Setup camera
cam = None
for i in range(10):
    test_cam = cv2.VideoCapture(i)
    if test_cam.isOpened():
        print(f"? Camera found at index {i}")
        cam = test_cam
        break

if cam is None:
    print("? No working camera found!")
    exit()

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
time.sleep(2)

if not cam.isOpened():
    print("? Error: Could not open camera.")
    cleanup_gpio()
    exit()

print("?? Looking for registered face...")

otp_sent = False
matched_number = None

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces_detected:
        roi_gray = gray[y:y + h, x:x + w]
        label, confidence = recognizer.predict(roi_gray)

        if confidence < 60:
            matched_number = label_to_mobile[label]
            cv2.putText(frame, "User Detected", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

            if not otp_sent:
                otp = str(random.randint(1000, 9999))
                client = Client(account_sid, auth_token)
                client.messages.create(
                    body=f"Smart Door Lock - Your OTP is: {otp}",
                    from_=twilio_number,
                    to=matched_number
                )
                otp_sent = True

                cam.release()
                cv2.destroyAllWindows()

                # OTP verification
                user_input = input("Enter the OTP: ")
                if user_input.strip() == otp:
                    print("? OTP matched. Unlocking door...")
                    unlock_sequence()
                else:
                    print("? Incorrect OTP. Access Denied.")
                cleanup_gpio()
                exit()
        else:
            cv2.putText(frame, "Unknown", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 0, 255), 2)

    cv2.imshow("Face Recognition with OTP", frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cam.release()
cv2.destroyAllWindows()
cleanup_gpio()
