import requests
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

stream_url = 'http://192.168.4.1:8888/stream'

response = requests.get(stream_url, stream=True)

if response.status_code == 200:
    bytes = b''
    for chunk in response.iter_content(chunk_size=1024):
        bytes += chunk
        a = bytes.find(b'\xff\xd8')  # JPEG start
        b = bytes.find(b'\xff\xd9')  # JPEG end
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]  # Actual JPEG bytes
            bytes = bytes[b+2:]  # Remaining bytes

            img = Image.open(BytesIO(jpg))
            frame = np.array(img)
            # Convert RGB to BGR
            frame = frame[:, :, ::-1].copy()
            
            # Now you can process the frame with OpenCV
            # For example, display the image
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
else:
    print(f'Failed to retrieve the stream. Status code: {response.status_code}')

cv2.destroyAllWindows()
