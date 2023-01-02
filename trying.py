import cv2
import numpy as np
cap = cv2.VideoCapture(0)
global x,y,paint
_, frame = cap.read()
old_gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#lucas kanade parameters
lk_params = dict(winSize = (15, 15),
maxLevel = 4,
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
#here taking the point from user so that it is tracks that object
def trackpoint(event,x,y,flags,params):
    global point,point_selected,old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point =(x,y)
        point_selected= True
        old_points = np.array([[x, y]],dtype=np.float32)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame",trackpoint)

point_selected=False
point=()
stp=0




while True:

    _, frame =cap.read()#newinpimage
    frame=cv2.flip(frame,1)
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    paint = np.zeros_like(frame)#mask
    if point_selected is True:
        cv2.circle(frame,point,5,(0,0,255),2)
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
        old_gray=gray_frame.copy()
        old_points=new_points
        x,y=new_points.ravel()
        for i,j in zip(old_points,new_points):
            x,y =j.ravel()
            a,b=i.ravel()
            if cv2.waitKey(2) & 0xff == ord('q'):
                stp = 1

            elif cv2.waitKey(2) & 0xff == ord('w'):
                stp = 0

            elif cv2.waitKey(2) == ord('n'):
                paint = np.zeros_like(frame)

            if stp == 0:
                paint = cv2.line(paint, (a, b), (x, y), (0, 0, 255), 6)

        cv2.circle(frame,(x,y),5,(0,255,0),-1)
        frame = cv2.addWeighted(paint, 0.3, frame, 0.7, 0)
        cv2.putText(paint, "'q' to gap 'w' - start 'n' - clear", (10, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))

    cv2.imshow("frame",frame)
    cv2.imshow("paint", paint)







    #break out program pressing esc
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()