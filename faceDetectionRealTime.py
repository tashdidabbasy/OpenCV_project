# If you want to run this code in your pc or laptop you need to istall Python, any python interpreter (I used Pycharm) and openCV libray. 


import cv2
# Importing OpenCV library

face_cscade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Reading the haar cascade xml file.

video = cv2.VideoCapture(0)
#Capturing video from default webcam

while True:
    #Video is nothing but some frequent image or frame. So we loop through the frames
    
    true,frame= video.read()
    #here true is for whether the camera is working good or not 

    frane_gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Gray image is for algorithm 
    
    face= face_cscade.detectMultiScale(frane_gray,scaleFactor=1.04,minNeighbors=6)
    for x,y,w,h in face:
        #x,y,w,h is the x- axis, y-axis, weight anf hight 
    
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame,"Face",(x,y+(w+30)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    
    cv2.imshow("Display",frame)
    #displaying the frames
    
    k= cv2.waitKey(1)
    #here each frame is displayed after every 1ms
    
    if k==27:
        #27 is the esc key
    
        break

video.release()
cv2.destroyAllWindows()
