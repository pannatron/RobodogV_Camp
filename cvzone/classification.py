from cvzone.ClassificationModule import Classifier
import cv2
from playsound import playsound
import threading

# สร้างตัวแปรแบบ global เพื่อตรวจสอบว่าเสียงกำลังเล่นอยู่หรือไม่
is_playing = False

def play_alert_sound():
    global is_playing
    is_playing = True
    playsound('videoplayback (1).mp4')
    is_playing = False
    print('Playing sound completed')

cap = cv2.VideoCapture(0)  # Initialize video capture
path = "converted_keras (2)/"
maskClassifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')

while True:
    _, img = cap.read()  # Capture frame-by-frame
    prediction = maskClassifier.getPrediction(img)
    print(prediction[1])  # Print prediction result
    if prediction[1] == 1 and not is_playing:
        # เรียกใช้ thread เพื่อเล่นเสียง ถ้าเสียงไม่ได้เล่นอยู่
        threading.Thread(target=play_alert_sound).start()
        print('Playing sound in a separate thread')

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for a key press to exit
        break

cap.release()
cv2.destroyAllWindows()
