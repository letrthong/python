#  pip install opencv-python

import cv2

rtsp_url = "rtsp://telua1:12345678@192.168.1.6:554/stream1"
cap = cv2.VideoCapture(rtsp_url)

# Initialize HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect people
    #boxes, _ = hog.detectMultiScale(frame, winStride=(8,8), padding=(8,8), scale=1.05)
    
    # Draw bounding boxes
    #for (x, y, w, h) in boxes:
    #    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Tapo C200 Stream", frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

