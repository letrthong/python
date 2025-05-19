import cv2

# Open the video stream (0 for webcam or use a stream URL)
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# 'VP80' is the FourCC code for VP8, which is used in WebM
fourcc = cv2.VideoWriter_fourcc(*'VP80')
out = cv2.VideoWriter('output.webm', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow('Recording', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
