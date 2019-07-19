import numpy as np
import cv2
l = 100
b = np.ones((l, l), dtype=np.float32)


def fuc(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b[y, x] = 1-b[y, x]
        print(x, y)
        cv2.imshow("Conway's Game of Life | Press any key when done making initial configuration", b)


cv2.namedWindow("Conway's Game of Life | Press any key when done making initial configuration",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Conway's Game of Life | Press any key when done making initial configuration", 600,600)
cv2.setMouseCallback("Conway's Game of Life | Press any key when done making initial configuration", fuc)
cv2.imshow("Conway's Game of Life | Press any key when done making initial configuration", b)
cv2.waitKey(0)

k = 0
while k == 0:
    c = np.copy(b)
    print(c)
    for i in range(1, l-1):
        for j in range(1, l-1):
            s = 8-(b[i-1][j-1]+b[i-1][j]+b[i-1][j+1]+b[i][j-1]+b[i][j+1]+b[i+1][j-1]+b[i+1][j+1]+b[i+1][j])
            if b[i][j] == 1:
                if s == 3:
                    c[i][j]=0
            else:
                if s > 3:
                    c[i][j] = 1
                elif s < 2:
                    c[i][j] =1
    b = np.copy(c)
    cv2.imshow("Conway's Game of Life | Press any key when done making initial configuration", b)
    cv2.waitKey(0)
