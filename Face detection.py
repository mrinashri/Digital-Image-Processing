import cv2

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    print(ret)
    A = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cascade_face.detectMultiScale(A, 1.3, 6)
    
    for (x,y,u,v) in face:
        cv2.rectangle(img, (x,y), (x + u, y + v), (255, 255, 0), 6)
        
    cv2.imshow('img', img)
    key = cv2.waitKey(30) & 0xff
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()