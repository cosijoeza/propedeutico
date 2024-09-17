import numpy as np
import cv2


def dibuja_linea(x, y, xfin, yfin):
    lineWidth = 1
    color = (255, 0, 0)
    # RIGHT
    if x < xfin:
        a = min(x, xfin)
        b = max(x, xfin)
        x = a
        xfin = b
        l = (xfin - x) // 3
        cv2.line(imagen, (x, y), (x + l, y), color, lineWidth)
        cv2.line(imagen, (x + l, y), (x + l, y - l), color, lineWidth)
        cv2.line(imagen, (x + l, y - l), (x + 2 * l, y - l), color, lineWidth)
        cv2.line(imagen, (x + 2 * l, y - l), (x + 2 * l, y), color, lineWidth)
        cv2.line(imagen, (x + 2 * l, y), (x + 3 * l, y), color, lineWidth)
    # LEFT
    if x > xfin:
        a = min(x, xfin)
        b = max(x, xfin)
        x = a
        xfin = b
        l = (xfin - x) // 3
        cv2.line(imagen, (x, y), (x + l, y), color, lineWidth)
        cv2.line(imagen, (x + l, y), (x + l, y + l), color, lineWidth)
        cv2.line(imagen, (x + l, y + l), (x + 2 * l, y + l), color, lineWidth)
        cv2.line(imagen, (x + 2 * l, y + l), (x + 2 * l, y), color, lineWidth)
        cv2.line(imagen, (x + 2 * l, y), (x + 3 * l, y), color, lineWidth)
    # UP
    if y > yfin:
        a = max(y, yfin)
        b = min(y, yfin)
        y = a
        yfin = b
        l = (yfin - y) // 3
        cv2.line(imagen, (x, y), (x, y + l), color, lineWidth)
        cv2.line(imagen, (x, y + l), (x + l, y + l), color, lineWidth)
        cv2.line(imagen, (x + l, y + l), (x + l, y + 2 * l), color, lineWidth)
        cv2.line(imagen, (x + l, y + 2 * l), (x, y + 2 * l), color, lineWidth)
        cv2.line(imagen, (x, y + 2 * l), (x, y + 3 * l), color, lineWidth)
    # DOWN
    if y < yfin:
        a = max(y, yfin)
        b = min(y, yfin)
        y = a
        yfin = b
        l = (yfin - y) // 3
        cv2.line(imagen, (x, y), (x, y + l), color, lineWidth)
        cv2.line(imagen, (x, y + l), (x - l, y + l), color, lineWidth)
        cv2.line(imagen, (x - l, y + l), (x - l, y + 2 * l), color, lineWidth)
        cv2.line(imagen, (x - l, y + 2 * l), (x, y + 2 * l), color, lineWidth)
        cv2.line(imagen, (x, y + 2 * l), (x, y + 3 * l), color, lineWidth)


def fractal(n, x, y, xfin, yfin):
    if n == 0:
        dibuja_linea(x, y, xfin, yfin)
    else:
        # RIGHT
        if x < xfin:
            l = (xfin - x) // 3
            print("AAA", n, x, y, xfin, yfin, l)
            fractal(n - 1, x, y, x + l, y)
            fractal(n - 1, x + l, y, x + l, y - l)
            fractal(n - 1, x + l, y - l, x + 2 * l, y - l)
            fractal(n - 1, x + 2 * l, y - l, x + 2 * l, y)
            fractal(n - 1, x + 2 * l, y, x + 3 * l, y)
        # LEFT
        if x > xfin:
            l = (x - xfin) // 3
            print("BBB", n, x, y, xfin, yfin, l)
            fractal(n - 1, x, y, x - l, y)
            fractal(n - 1, x - l, y, x - l, y + l)
            fractal(n - 1, x - l, y + l, x - 2 * l, y + l)
            fractal(n - 1, x - 2 * l, y + l, x - 2 * l, y)
            fractal(n - 1, x - 2 * l, y, x - 3 * l, y)
        # UP
        if y > yfin:
            l = (y - yfin) // 3
            print("CCC", n, x, y, xfin, yfin, l)
            fractal(n - 1, x, y, x, y - l)
            fractal(n - 1, x, y - l, x - l, y - l)
            fractal(n - 1, x - l, y - l, x - l, y - 2 * l)
            fractal(n - 1, x - l, y - 2 * l, x, y - 2 * l)
            fractal(n - 1, x, y - 2 * l, x, y - 3 * l)
        # DOWN
        if y < yfin:
            l = (yfin - y) // 3
            print("DDD", n, x, y, xfin, yfin, l)
            fractal(n - 1, x, y, x, y + l)
            fractal(n - 1, x, y + l, x + l, y + l)
            fractal(n - 1, x + l, y + l, x + l, y + 2 * l)
            fractal(n - 1, x + l, y + 2 * l, x, y + 2 * l)
            fractal(n - 1, x, y + 2 * l, x, y + 3 * l)


height = 1000
width = 1000
channels = 3

imagen = 255 * np.ones((height, width, channels), dtype=np.uint8)

# GBR

# UP
#fractal(0,100,400,829,400)
#fractal(1,100,400,829,400)
# fractal(2,100,400,829,400)
# fractal(3,100,400,829,400)
fractal(4,100,400,829,400)

# DOWN
fractal(4,829,400,100,400)
#fractal(1,829,400,100,400)

# RIGTH
#fractal(0,400,100,400,829)
fractal(4,400,100,400,829)
# fractal(1,400,100,400,829)

# LEFT
fractal(4,400,829,400,100)
# fractal(0,400,829,400,100)
# fractal(1,400,829,400,100)

cv2.imshow("imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
