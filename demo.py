from TIS import TIS
import cv2

cap = TIS.VideoCapture(0)
while True:
  ret, frame = cap.read()
  if ret:
    cv2.imshow('Demo', frame)
    if cv2.waitKey(1) == ord('q'):
      break
