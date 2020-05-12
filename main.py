import cv2 as cv
import os
import sys
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow import keras

sys.path.append('./classes')
from classes import Recognition
from classes import Correct
from classes import Window
from Recognition import *
from Correct import *
from Window import *

def main():
    fnFrame = 'image_3_green.png'
    fnFrame = 'pngOne4.png'
    fnModel = 'image_3_green.png'

    frame = cv.imread(fnFrame)
    model = cv.imread(fnModel)

    #i = input("Manual debug hsv? (y/n)\n")
    #if i == "y":
    #    #while True:
    #    Recognition().GetHsvMinMax(frame)
    #        #if cv.waitKey(1) & 0xFF == ord('q'):
    #    return 0
    
    hsv_all = Recognition().InsertColor()

    arrRects = Recognition().GetRectangles(frame, hsv_all)
    Recognition().GetQR(frame, arrRects)

    Window().PrintContoursRect(frame, arrRects)
    Window().PrintCoordsRect(frame, arrRects)

    Correct().IsSamePlane(arrRects)

    while True:
        Window().ShowWindow(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    return 0



if __name__ == '__main__':
    main()
