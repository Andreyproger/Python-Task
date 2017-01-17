import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  lower_blue = np.array([110,50,50])
  upper_blue = np.array([130,255,255])
  
  hsv_raw = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
  hsv_modified  =  cv2.inRange(hsv, lower_blue, upper_blue)
  hsv_modified  =  cv2.medianBlur(hsv_modified, 9)
  
  contours, hierarchy = cv2.findContours(hsv_modified,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  areas = [cv2.contourArea(c) for c in contours]
  if areas: # if  not empty
    max_index = np.argmax(areas)
    cnt=contours[max_index]

    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)



  cv2.imshow('frame',frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
