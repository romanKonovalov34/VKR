import cv2 as cv
import os
import sys
from tkinter import *
import numpy as np
from PIL import Image, ImageTk

class Window:
    def PrintContoursRect(self, frame, arrRects):
        cv.drawContours(frame, arrRects, -1, (255,0,0), 1, cv.LINE_AA) # рисуем прямоугольник
            

    def PrintCoordsRect(self, frame, arrRects):
        color = (0,0,0)
        for i in range(len(arrRects)):
            for j in range(len(arrRects[i])):
                cv.putText(frame, str((arrRects[i][j][0], arrRects[i][j][1])) , (arrRects[i][j][0], arrRects[i][j][1]), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)


    def ShowWindow(self, frame):
        cv.imshow("Res", frame)
        # root = Tk()
        # root.title("Вывод")
        # # root.geometry("1024x640")

        # photo = ImageTk.PhotoImage(image = Image.fromarray(frame)) # преобразуем изобжаение из массива NumPy в PhotoImage
        # label = Label(image=photo)
        # label.image = photo # получили ссылку
        # label.pack()

        # root.mainloop()


        #!!!!! имеет место быть функции render