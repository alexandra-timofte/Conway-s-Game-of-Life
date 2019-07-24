import numpy as np
import cv2
lg = 100
d = 50
k = lg + 2*d
# lg = lungimea matricei afisate
# d este lungimea marginii, lg+2*d e lungimea matricei mari
b = np.ones((lg+2*d, lg+2*d), dtype=np.float32)
af = b[d:d+lg, d:d+lg]
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

# cu vectorizare
t = 0
while t == 0:
    c = np.copy(b)
    print(c)
    vl = np.ones((1, k))
    vh = np.ones((k, 1))

    sus = np.copy(b[1:, :])
    sus = np.vstack((sus, vl))

    jos = np.copy(b[:k-1, :])
    jos = np.vstack((vl, jos))

    stg = np.copy(b[:, 1:])
    stg = np.hstack((stg, vh))

    drp = np.copy(b[:, :k-1])
    drp = np.hstack((vh, drp))

    d1 = np.copy(sus[:, 1:])
    d1 = np.hstack((d1, vh))

    d2 = np.copy(sus[:, :k-1])
    d2 = np.hstack((vh, d2))

    d3 = np.copy(jos[:, 1:])
    d3 = np.hstack((d3, vh))

    d4 = np.copy(jos[:, :k-1])
    d4 = np.hstack((vh, d4))

    s = 8-(sus+jos+drp+stg+d1+d2+d3+d4)
    b = np.array(b)
    s = np.array(s)
    bl = b == 1
    b3 = s == 3
    bl = np.array(bl)
    b3 = np.array(b3)
    bt1 = bl*b3
    bt1 = bt1.astype(bool)
    c[bt1] = 0

    bn = 1-(s <= 3)*(s >= 2)
    bn = np.array(bn)
    blo = b == 0
    blo = np.array(blo)
    bt2 = bn*blo
    bt2= bt2.astype(bool)
    c[bt2] = 1

    b = np.copy(c)
    af = b[d:d + lg, d:d + lg]
    cv2.imshow(name, af)
    a = cv2.waitKey(0)
    print(a)
    if a == ord('s'):
        t = 1
