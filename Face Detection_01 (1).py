pip install numpyimport numpy as np
import cv2 

cap = cv2.VideoCapture(0)

while True:
    
    succes, img = cap.read()
    
    if succes:
        
        width = int(cap.get(3))
        height = int(cap.get(4))
        
        img = cv2.line(img, (100, 400), (500, 400), (255, 0, 0), 5)
        
        img = cv2.rectangle(img, (160, 60), (400, 350), (255, 255, 255), 3)
        
        img = cv2.circle(img, (280, 550), 100, (255, 255, 255), 3)
        
        
        img = cv2.putText(img, "Python Programer", (45, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)
        
        
        
        cv2.imshow('img', img)
        
    if cv2.waitKey(25) == ord("q"):break
    
cap.release()
cv2.destroyAllWindows()

    
    
