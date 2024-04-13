import asyncio
from bleak import BleakClient
from cvzone.HandTrackingModule import HandDetector
import cv2
import time

# UUIDs for connection and characteristic
# uuid = "110FD977-BA0B-8056-23CD-F5EA9B3F8524"
# characteristic_uuid = "0000ffe2-0000-1000-8000-00805f9b34fb"
uuid = "EA9EA3F3-42F7-4037-142D-FBD1FC4962B3"
characteristic_uuid = "0000ffe1-0000-1000-8000-00805f9b34fb"

client = None  # Global variable for BLE client

async def connect_to_petoi():
    global client
    client = BleakClient(uuid)
    try:
        await client.connect()
        if client.is_connected:
            print("Connected to Petoi")
            return True
        else:
            print("Failed to connect to Petoi")
            return False
    except Exception as e:
        print(f"Error connecting to Petoi: {e}")
        return False

async def send_command(command):
    if client and client.is_connected:
        try:
            print(f"Sending command: {command}")
            await client.write_gatt_char(characteristic_uuid, command.encode())
            print(f"Sent command '{command}' to Petoi")
        except Exception as e:
            print(f"Error sending command to Petoi: {e}")

def main():
    # Connect to Petoi
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect_to_petoi())
    # Delay for 10 seconds
    time.sleep(10)

    cap = cv2.VideoCapture(0)
    detector = HandDetector(staticMode=False, maxHands=4, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

    last_timestamp = time.time()  # กำหนดค่าเริ่มต้นที่นี่
    last_timescheck = time.time()
    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img, draw=True, flipType=True)
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
                    cv2.putText(img, "Boxing", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Boxing", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("kbx"))

                elif is_max_x_at_4 and is_max_y_at_4  and is_min_y_at_12  :
                    cv2.putText(img, "Hug", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Hug", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("khg"))

                elif is_min_x_at_4 and is_second_smallest_y_at_4  and is_min_y_at_8 :
                    cv2.putText(img, "Stand Up", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Stand Up", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("kbalance"))

                
                elif is_max_x_at_4 and is_max_y_at_8  :
                    cv2.putText(img, "Sit", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Sit", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("ksit"))

                elif is_min_x_at_4 and is_max_x_at_8  :
                    cv2.putText(img, "hi", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "hi", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("kfiv"))

                elif is_min_x_at_8 and is_max_x_at_4  :
                    cv2.putText(img, "Push up", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Push up", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("kpu"))

                elif is_min_x_at_4 and is_min_y_at_4 and is_max_y_at_12 :
                    cv2.putText(img, "Joy", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Joy", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("kchr"))

                elif is_max_x_at_4 and is_min_y_at_4 and is_max_y_at_12 :
                    cv2.putText(img, "Rest", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
                    last_timestamp = time.time()
                    if time.time()-last_timescheck >1 :
                        cv2.putText(img, "Rest", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5)
                        loop.run_until_complete(send_command("d"))



        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Disconnect from Petoi
    if client:
        loop.run_until_complete(client.disconnect())

if __name__ == "__main__":
    main()
