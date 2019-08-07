import numpy as np
import cv2
lg = 100
d = 50
# lg = lungimea matricei afisate
# d este lungimea marginii, lg+2*d e lungimea matricei mari
b = np.ones((lg+2*d, lg+2*d), dtype=np.float32)
af = b[d:d+lg, d:d+lg]
print(af)
name = "Conway's Game of Life | Press any key when done making initial configuration"


def fuc(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b[y+d, x+d] = 1-b[y+d, x+d]
        print(x, y)
        cv2.imshow(name, af)


cv2.namedWindow(name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(name, 600, 600)
cv2.setMouseCallback(name, fuc)
cv2.imshow(name, af)
cv2.waitKey(0)

k = 0
while k == 0:
    c = np.copy(b)
    print(c)
    for i in range(1, lg+2*d-1):
        for j in range(1, lg+2*d-1):
            s = 8-(b[i-1][j-1]+b[i-1][j]+b[i-1][j+1]+b[i][j-1]+b[i][j+1]
                   + b[i+1][j-1]+b[i+1][j+1]+b[i+1][j])
            if b[i][j] == 1:
                if s == 3:
                    c[i][j] = 0
            else:
                if s > 3:
                    c[i][j] = 1
                elif s < 2:
                    c[i][j] = 1
    b = np.copy(c)
    af = b[d:d + lg, d:d + lg]
    cv2.imshow(name, af)
    a = cv2.waitKey(0)
    print(a)
    if a == ord('s'):
        k = 1
