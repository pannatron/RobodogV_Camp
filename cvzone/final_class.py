from cvzone.HandTrackingModule import HandDetector
import cv2
import time
def get_max_area_hand(hands):
    max_area = 0
    max_area_hand = None

    for hand in hands:
        bbox = hand["bbox"]
        area = bbox[2] * bbox[3]

        if area > max_area:
            max_area = area
            max_area_hand = hand

    return max_area_hand
# file_path = "./captured_image.jpg" 
# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
# image = cv2.imread(file_path)
# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False,
                        maxHands=4,
                        modelComplexity=1,
                        detectionCon=0.5,
                        minTrackCon=0.5)

# Continuously get frames from the webcam

last_timestamp = time.time()
last_timescheck = time.time()

while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()

    hands, img = detector.findHands(img, draw=True, flipType=True)
    # start_time = int(time.time())
    # while True:
    #     if (int(time.time()) - start_time) > 5:
    #         break
        
    if hands:
        lm_list = hands[0].get('lmList')
        if len(lm_list) >= 21:  # Ensure that there are enough points in lm_list
            reference_x_come = lm_list[4][0]
            reference_y_come = lm_list[4][1]

            x_values = [lm_list[i][0] for i in [4, 8, 12, 16, 20]]
            y_values = [lm_list[i][1] for i in [4, 8, 12, 16, 20]]
            print(y_values)
            print("ylist value")
            if time.time() - last_timestamp > 0.1:
                last_timescheck = time.time()


            # Check specific indices (4, 8, 12, 16, and 20) for min x and max y
            is_min_x_come = reference_x_come <= lm_list[4][0] and reference_x_come <= lm_list[8][0] and reference_x_come <= lm_list[12][0] and reference_x_come <= lm_list[16][0] and reference_x_come <= lm_list[20][0]
            is_max_y_come = reference_y_come >= lm_list[4][1] and reference_y_come >= lm_list[8][1] and reference_y_come >= lm_list[12][1] and reference_y_come >= lm_list[16][1] and reference_y_come >= lm_list[20][1]

            # Additional condition for min x and min y at index 12
            is_min_x_at_12 = reference_x_come == min(lm_list[4][0], lm_list[8][0], lm_list[12][0], lm_list[16][0], lm_list[20][0])
            is_min_y_at_12 = lm_list[12][1] == min(lm_list[4][1], lm_list[8][1], lm_list[12][1], lm_list[16][1], lm_list[20][1])

            is_max_x_at_12 =  lm_list[12][0] == max(lm_list[4][0], lm_list[8][0], lm_list[12][0], lm_list[16][0], lm_list[20][0])
            is_max_y_at_12 = lm_list[12][1] == max(lm_list[4][1], lm_list[8][1], lm_list[12][1], lm_list[16][1], lm_list[20][1])


            is_max_x_at_4 = lm_list[4][0] == max(lm_list[4][0], lm_list[8][0], lm_list[12][0], lm_list[16][0], lm_list[20][0])
            is_max_y_at_4 = lm_list[4][1] == max(lm_list[4][1], lm_list[8][1], lm_list[12][1], lm_list[16][1], lm_list[20][1])
            
            is_min_x_at_4 = lm_list[4][0] == min(lm_list[4][0], lm_list[8][0], lm_list[12][0], lm_list[16][0], lm_list[20][0])
            is_min_y_at_4 = lm_list[4][1] == min(lm_list[4][1], lm_list[8][1], lm_list[12][1], lm_list[16][1], lm_list[20][1])
            
            is_max_x_at_8 = lm_list[8][0] == max(lm_list[8][0], lm_list[8][0], lm_list[12][0], lm_list[16][0], lm_list[20][0])
            is_max_y_at_8 = lm_list[8][1] == max(lm_list[8][1], lm_list[8][1], lm_list[12][1], lm_list[16][1], lm_list[20][1])

            is_min_x_at_8 = lm_list[8][0] == min(lm_list[8][0], lm_list[8][0], lm_list[12][0], lm_list[16][0], lm_list[20][0])
            is_min_y_at_8 = lm_list[8][1] == min(lm_list[8][1], lm_list[8][1], lm_list[12][1], lm_list[16][1], lm_list[20][1])
            second_smallest_x = sorted(x_values)[1]
            second_smallest_y = sorted(y_values)[1]

            # Check if the points at index 4 have the second smallest x and y values
            is_second_smallest_x_at_4 = lm_list[4][0] == second_smallest_x
            is_second_smallest_y_at_4 = lm_list[4][1] == second_smallest_y


            if is_min_x_come and is_max_y_come  and is_min_y_at_12  :
                cv2.putText(img, "Come", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "Come", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                
            elif is_max_x_at_4 and is_max_y_at_4  and is_min_y_at_12  :
                cv2.putText(img, "Stop", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "Stop", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
            elif is_min_x_at_4 and is_second_smallest_y_at_4  and is_min_y_at_8 :
                cv2.putText(img, "Stand Up", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "Stand Up", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
            elif is_max_x_at_4 and is_max_y_at_8  :
                cv2.putText(img, "Sit", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "Sit", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
            elif is_min_x_at_4 and is_max_x_at_8  :
                cv2.putText(img, "turn left", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "turn left", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
            elif is_min_x_at_8 and is_max_x_at_4  :
                cv2.putText(img, "turn Right", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "turn Right", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)

            elif is_min_x_at_4 and is_min_y_at_4 and is_max_y_at_12 :
                cv2.putText(img, "Joy", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "Joy", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
            elif is_max_x_at_4 and is_min_y_at_4 and is_max_y_at_12 :
                cv2.putText(img, "Hand tracking", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                last_timestamp = time.time()
                if time.time()-last_timescheck >3 :
                    cv2.putText(img, "Hand tracking", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)


            # lm_list = hands[0].get('lmList')
            # for i, lm in enumerate(lm_list):
            #     x, y = lm[0], lm[1]
            #     text = f"P: {i}"
            #     cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

            #cv2.putText(img, "text", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            biggestHand = get_max_area_hand(hands)
            fingers = detector.fingersUp(biggestHand)
            print('H1 : ',fingers.count(1))
            cv2.imshow("Image", img)
            # while True:
            #     if (int(time.time()) - start_time) > 5:
            #         break


            
    # Display the image in a window
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)  # Wait for a key press (1 millisecond delay)
    
    # Close the window if the 'q' key is pressed
    if key == ord('q'):
        break
    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    # cv2.waitKey(1)
