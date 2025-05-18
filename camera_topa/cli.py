#  pip install opencv-python

import cv2

rtsp_url = "rtsp://telua1:12345678@192.168.1.6:554/stream1"
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Tapo C200 Stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

