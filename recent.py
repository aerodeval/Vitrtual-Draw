import cv2
import numpy as np
import sys
x, y, k = 200, 200, -1

cap = cv2.VideoCapture(0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 255, 255), (139, 0, 139),(30,105,210),(0,0,0)]


def track(event, x1, y1, flag, param):
    global x, y, k
    if event == cv2.EVENT_LBUTTONDOWN:
        x = x1
        y = y1
        k = 1
    if cv2.waitKey(2) & 0xff == ord('j'):
        x=200
        y=200


cv2.namedWindow("enter_point")
cv2.setMouseCallback("enter_point", track)

while True:

    _, inp_img = cap.read()
    inp_img = cv2.flip(inp_img, 1)
    a=cv2.COLOR_BGR2GRAY
    gray_inp_img = cv2.cvtColor(inp_img,a)

    cv2.imshow("enter_point", inp_img)

    if k == 1 or cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break

stp = 0
old_pts = np.array([[x, y]], dtype=np.float32).reshape(-1, 1, 2)

mask = cv2.imread(sys.argv[1])

while True:
    _, new_inp_img = cap.read()
    new_inp_img = cv2.flip(new_inp_img, 1)
    new_gray = cv2.cvtColor(new_inp_img, cv2.COLOR_BGR2GRAY)
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(gray_inp_img,
                                                    new_gray,
                                                    old_pts,
                                                    None, maxLevel=5,
                                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                                                              15, 15))

    for i, j in zip(old_pts, new_pts):
        x, y = j.ravel()
        a, b = i.ravel()
        if cv2.waitKey(2) & 0xff == ord('0'):
            stp = 1

        elif cv2.waitKey(2) & 0xff == ord('.'):
            stp = 0

        elif cv2.waitKey(2) == ord('n'):
            mask = cv2.imread('C:/Users/wgome/Desktop/qtdesigner/MOVING DISK.PNG')

        if stp == 0:
            mask = cv2.line(mask, (a, b), (x, y), colors[0], 6)
            if cv2.waitKey(2) & 0xff == ord('2'):
                colors[0] = colors[1]
                mask = cv2.line(mask, (a, b), (x, y), colors[1], 6)
            elif cv2.waitKey(2) & 0xff == ord('3'):
                colors[0] = colors[2]
                mask = cv2.line(mask, (a, b), (x, y), colors[2], 6)
            elif cv2.waitKey(2) & 0xff == ord('4'):
                colors[0] = colors[3]
                mask = cv2.line(mask, (a, b), (x, y), colors[2], 6)
            elif cv2.waitKey(2) & 0xff == ord('5'):
                colors[0] = colors[4]
                mask = cv2.line(mask, (a, b), (x, y), colors[2], 6)
            elif cv2.waitKey(2) & 0xff == ord('6'):
                colors[0] = colors[5]
                mask = cv2.line(mask, (a, b), (x, y), colors[2], 6)
            elif cv2.waitKey(2) & 0xff == ord('7'):
                colors[0] = colors[6]
                mask = cv2.line(mask, (a, b), (x, y), colors[2], 6)
            elif cv2.waitKey(2) & 0xff == ord('8'):
                colors[0] = colors[7]
                mask = cv2.line(mask, (a, b), (x, y), colors[2], 6)

        cv2.circle(new_inp_img, (x, y), 6, (0, 255, 0), -1)

    cv2.putText(mask, "'0' to gap '.' - continue 'n' - clear", (10, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow("ouput", new_inp_img)
    cv2.imshow("Paint", mask)

    gray_inp_img = new_gray.copy()
    old_pts = new_pts.reshape(-1, 1, 2)

    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
cap.release()
