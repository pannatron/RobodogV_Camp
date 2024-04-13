import cv2
import time


video=cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Could not openvideo.")
    exit() 
    
frame_counter=0
start_time=time.time()

while True:
    ret,frame = video.read()
    frame_counter+=1
    time_elaped=time.time()-start_time
    fps= frame_counter/time_elaped
    cv2.putText(frame,f"FPS:{fps:.2f}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)   
    cv2.imshow('Video',frame)
    
    if time_elaped >1.0:
        frame_counter=0
        start_time=time.time()
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
video.release()
cv2.destroyAllWindows()