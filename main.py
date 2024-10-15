from TIS import TIS
import numpy as np
import cv2

cap1 = TIS.VideoCapture(0)
cap2 = TIS.VideoCapture(1)
while True:
  ret1, frame1 = cap1.read()
  ret2, frame2 = cap2.read()
  if ret1 and ret2:
    frame_merged = np.hstack((frame1, frame2))
    frame_merged = cv2.resize(frame_merged, (900, 256), interpolation=cv2.INTER_AREA)
    
    cv2.imshow('Demo', frame_merged)
    if cv2.waitKey(1) == ord('q'):
      break
