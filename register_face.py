import cv2
import os
import time

CASCADE_PATH = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def find_working_camera():
    for i in range(4):  # Usually 0-3 is enough
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            return i
    return None

cam_index = find_working_camera()
if cam_index is None:
    print("? No working camera found. Check connection.")
    exit()
else:
    print(f"?? Using /dev/video{cam_index}")

mobile_number = input("Enter your mobile number (e.g., +91xxxxxxxxxx): ")

# Create user-specific folder
user_folder = os.path.join("dataset", mobile_number)
os.makedirs(user_folder, exist_ok=True)

# Save number.txt inside folder
with open(os.path.join(user_folder, "number.txt"), "w") as f:
    f.write(mobile_number)

print("? Initializing camera...")
time.sleep(2)

count, max_images = 0, 20
cap = cv2.VideoCapture(cam_index)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("?? Capturing face images... Press 'q' to quit early.")

while count < max_images:
    ret, frame = cap.read()

    if not ret:
        print("?? Frame grab failed, retrying...")
        cap.release()
        time.sleep(1)
        cap = cv2.VideoCapture(cam_index)
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]
        filename = os.path.join(user_folder, f"{count}.jpg")
        cv2.imwrite(filename, face_img)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print(f"? Saved {filename}")
        time.sleep(0.3)

        if count >= max_images:
            break

    cv2.imshow("Register Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("?? Registered face images saved.")
