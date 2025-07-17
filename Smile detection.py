import cv2

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    A = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cascade_face.detectMultiScale(A, scaleFactor= 1.3, minNeighbors= 5, minSize = (30,30))
    
    for (x,y,u,v) in face:
        cv2.rectangle(img, (x,y), (x + u, y + v), (255, 255, 0), 2)
        gray_rect = A[y : y + v, x : x + u]
        
        smile = cascade_smile.detectMultiScale(gray_rect, scaleFactor= 1.5, minNeighbors= 15, minSize= (25,25))
        
        for i in smile:
            if len(smile) > 1:
                cv2.putText(img, "SMILE DETECTED", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3, cv2.LINE_AA)
                
    cv2.imshow('video', img)
    key = cv2.waitKey(30) & 0xff
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()