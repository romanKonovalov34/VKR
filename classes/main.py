# -*- coding: utf-8 -*-

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
from classes import Process
from Recognition import *
from Correct import *
from Window import *
from Process import *

def rotateImage(image, angle):
     image_center = tuple(np.array(image.shape[1::-1]) / 2)
     rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
     result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
     return result

 
def Process():

    cap = cv.VideoCapture('test1.MOV')

    # тут hsv для всех цветов кубиков
    hsv_all = Recognition().InsertColor()


    while True:

        ret, frame = cap.read()
        
        # обрабатываю видео с телефона, но сдесь выводится "вверх ногами", поэтому переворачиваю кадры
        frame = rotateImage(frame, 180)
        #frame = cv.imread('123Second.png')

        # Запись fullHD и слишком большой масштаб кадра, делаю fullHD/2
        #frame = cv.resize(frame, (960, 540))
        frame = cv.resize(frame, (640, 360))
        #frame = cv.resize(frame, (320, 180))

        if cv.waitKey(1) & 0xFF == ord('g'):
    

            arrRects = Recognition().GetRectangles(frame, hsv_all)

            if len(arrRects) > 0:

                print('Count rects: ', len(arrRects))

                Recognition().GetQR(frame, arrRects)


                #Window().PrintContoursRect(frame, arrRects)
                #Window().PrintCoordsRect(frame, arrRects)
                #Window().PrintCountRects(frame, arrRects)


            #    #Correct().IsSamePlane(arrCodes)

        Window().ShowWindow(frame, targetImg)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    

        



def main():

    #fnFrame = 'gry.png'
    #frame = cv.imread(fnFrame)
    
    #i = input("Manual debug hsv? (y/n)\n")
    #if i == "y":
    #    #while True:
    #    Recognition().GetHsvMinMax(frame)
    #        #if cv.waitKey(1) & 0xFF == ord('q'):
    #    return 0

    cap = cv.VideoCapture('test1.MOV')

    # тут hsv для всех цветов кубиков
    hsv_all = Recognition().InsertColor()


    
    # обработка шаблонного изображения единожды
    targetImg = cv.imread('targetAssembly.png')
    arrRectsTarget = Recognition().GetRectangles(targetImg, hsv_all)

    if len(arrRectsTarget) > 0:

        #print('Count rects: ', len(arrRects))

        Recognition().GetQR(targetImg, arrRectsTarget)


        #Window().PrintContoursRect(targetImg, arrRects)
        #Window().PrintCoordsRect(frame, arrRects)
        #Window().PrintCountRects(targetImg, arrRects)

        resizedTargeImg = cv.resize(targetImg, (500, 500))
        cv.imwrite('tkimgTarget.png', resizedTargeImg)




    #while True:

    #    ret, frame = cap.read()
        
    #    # обрабатываю видео с телефона, но сдесь выводится "вверх ногами", поэтому переворачиваю кадры
    #    frame = rotateImage(frame, 180)
    #    #frame = cv.imread('123Second.png')

    #    # Запись fullHD и слишком большой масштаб кадра, делаю fullHD/2
    #    #frame = cv.resize(frame, (960, 540))
    #    frame = cv.resize(frame, (640, 360))
    #    #frame = cv.resize(frame, (320, 180))

    #    if cv.waitKey(1) & 0xFF == ord('g'):
    

    #        arrRects = Recognition().GetRectangles(frame, hsv_all)

    #        if len(arrRects) > 0:

    #            print('Count rects: ', len(arrRects))

    #            Recognition().GetQR(frame, arrRects)


    #            #Window().PrintContoursRect(frame, arrRects)
    #            #Window().PrintCoordsRect(frame, arrRects)
    #            #Window().PrintCountRects(frame, arrRects)


    #        #    #Correct().IsSamePlane(arrCodes)

    #    Window().ShowWindow(frame, targetImg)
        
    #    if cv.waitKey(1) & 0xFF == ord('q'):
    #        break
    
    #return 0



if __name__ == '__main__':
    main()
