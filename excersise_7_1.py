import cv2

# Initialize video capture with the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a single frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
