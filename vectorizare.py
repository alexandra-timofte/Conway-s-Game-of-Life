import numpy as np
import cv2
from scipy import signal


def test_main():
    lg = 30
    d = 2000
    # lg = lungimea matricei afisate
    # d este lungimea marginii, lg+2*d e lungimea matricei mari
    b = np.ones((lg+2*d, lg+2*d), dtype=np.float32)
    af = b[d:d+lg, d:d+lg]
    name = "Conway's Game of Life | Press any key when done making initial configuration"

    def fuc(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            b[y+d, x+d] = 1-b[y+d, x+d]
            print(x, y)
            cv2.imshow(name, af)

    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 600, 600)
    cv2.setMouseCallback(name, fuc)
    cv2.imshow(name, af)
    cv2.waitKey(0)
    t = 0
    while t == 0:
        s = np.zeros(b.shape)
        w = np.array([[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1], ], dtype='float')
        f = signal.convolve2d(b, w, 'valid')
        f = 8 - f
        s[1:-1, 1:-1] += f
        b[(b == 1) & (s == 3)] = 0
        b[((s > 3) | (s < 2)) & (b == 0)] = 1

        af = b[d:d + lg, d:d + lg]
        cv2.imshow(name, af)
        v = cv2.waitKey(0)
        if v == ord('s'):
            t = 1


if __name__ == "__main__":
    test_main()
