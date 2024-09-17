import cv2 as cv
import numpy as np


def dibuja_linea(x, y, xfin, yfin):
    lineWidth = 3
    l = (xfin - x) // 3
    cv.line(imagen, (x, y), (x + l, y), (255, 0, 0), lineWidth)
    cv.line(imagen, (x + l, y), (x + l, y - l), (255, 0, 0), lineWidth)
    cv.line(imagen, (x + l, y - l), (x + 2 * l, y - l), (255, 0, 0), lineWidth)
    cv.line(imagen, (x + 2 * l, y - l), (x + 2 * l, y), (255, 0, 0), lineWidth)
    cv.line(imagen, (x + 2 * l, y), (x + 3 * l, y), (255, 0, 0), lineWidth)


height = 1000
width = 1000
channels = 3

imagen = 255 * np.ones((height, width, channels), dtype=np.uint8)
print(imagen)

# GBR
dibuja_linea(100, 400, 829, 400)

cv.imshow("imagen", imagen)
cv.waitKey(0)
cv.destroyAllWindows()
