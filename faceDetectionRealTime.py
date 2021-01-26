import cv2
face_cscade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    true,frame= video.read()
    frane_gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face= face_cscade.detectMultiScale(frane_gray,scaleFactor=1.04,minNeighbors=6)
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame,"Face",(x,y+(w+30)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    cv2.imshow("Display",frame)
    k= cv2.waitKey(1)
    if k==27:
        break

video.release()
cv2.destroyAllWindows()