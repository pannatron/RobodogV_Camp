from cvzone.ClassificationModule import Classifier
from cvzone.PoseModule import PoseDetector
import cv2
from playsound import playsound
import threading

# สร้างตัวแปรแบบ global เพื่อตรวจสอบว่าเสียงกำลังเล่นอยู่หรือไม่
is_playing = False

def play_alert_sound():
    global is_playing
    is_playing = True
    playsound('videoplayback (1).mp4')  # แก้ไขเป็นชื่อไฟล์เสียงที่ถูกต้อง
    is_playing = False
    print('Playing sound completed')

cap = cv2.VideoCapture(0)  # Initialize video capture
path = "converted_keras/"
maskClassifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

while True:
    success, img = cap.read()  # Capture frame-by-frame
    if not success:
        break

    # ทำการประมวลผลด้วยการจำแนกประเภทก่อน
    prediction = maskClassifier.getPrediction(img)
    print(prediction[1])  # Print prediction result
    if prediction[1] == 1 and not is_playing:
        # เรียกใช้ thread เพื่อเล่นเสียง ถ้าเสียงไม่ได้เล่นอยู่
        threading.Thread(target=play_alert_sound).start()
        print('Playing sound in a separate thread')

    # ต่อไปคือการตรวจจับท่าทาง
    img = detector.findPose(img, draw=False)  # ตั้งค่า draw=False ถ้าคุณไม่ต้องการวาดโครงร่างท่าทาง
    lmList, bboxInfo = detector.findPosition(img, draw=False)  # ตั้งค่า draw=False ตามที่คุณต้องการ

    # เพิ่มโค้ดการตรวจจับท่าทางที่คุณต้องการทำตรงนี้

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for the 'q' key to stop the loop
        break

cap.release()
cv2.destroyAllWindows()
