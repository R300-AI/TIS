from TIS import TIS
import cv2

cap = TIS.VideoCapture(0)  #Indexing devices by order.
while True:
  ret, frame = cap1.read()
  if ret:
    cv2.imshow('Demo', frame)
    if cv2.waitKey(1) == ord('q'):
      break
