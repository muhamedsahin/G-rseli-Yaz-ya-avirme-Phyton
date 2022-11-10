import cv2
import pytesseract
import time
import keyboard

cam = cv2.VideoCapture(1)
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
sure = 0
font = cv2.FONT_HERSHEY_TRIPLEX
org = (50, 50)
fontScale = 1
color = (0, 0, 0)
thickness = 2
metin = "Yazı Yok"
Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
while True:
      ret, frame = cam.read()
      if keyboard.is_pressed('w'):
         metin = pytesseract.image_to_string(frame)
         if len(metin) > 0:
            metin = metin.translate(Tr2Eng)
            print(metin)
      frame = cv2.putText(frame, metin, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
      cv2.imshow('frame', frame)
      if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
