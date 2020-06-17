import cv2 as cv
import os
import sys
from tkinter import filedialog
from tkinter import *
#import tkinter as tk
#import tkinter.ttk as ttk
from tkinter import filedialog as fd

sys.path.append('./classes')
from classes import Correct
from classes import Processing
from Main import *

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

    def PrintCountRects(self, frame, arrRects):
        color = (0,0,0)
        cv.putText(frame, 'Count rectangles: ' + str(len(arrRects)), (30, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)



    def ShowWindow(self, frame, targetImg):





        #cv.imshow("res", frame)

        

        #root = tk()
        #root.title("вывод")
        ##root.geometry("1024x640")
        #root.geometry("1210x750")

        ## btns

        #loadbtn = button(text="загрузить целевую сборку")
        #updatebtn = button(text="обновить этап")

        #loadbtn.place(x=10, y=10)
        #updatebtn.place(x=180, y=10)


        ## label img

        #img = image.open("tkimg.png")
        #render = imagetk.photoimage(img)
        #labelimg0 = label(root, image=render)
        #labelimg0.image = render
        #labelimg0.place(relx=.0, rely=.065)

        #labelimg1 = label(root, image=render)
        #labelimg1.image = render
        #labelimg1.place(relx=.333, rely=.065)

        #labelimg2 = label(root, image=render)
        #labelimg2.image = render
        #labelimg2.place(relx=.666, rely=.065)

        
        ## label text

        #label0 = label(text="целевая сборка", justify=left)
        #label0.place(relx=.130, rely=.6)

        #label1 = label(text="текущая сборка", justify=left)
        #label1.place(relx=.460, rely=.6)

        #label2 = label(text="графическая отладка", justify=left)
        #label2.place(relx=.794, rely=.6)

        ##label3 = label(text="текстовая отладка", justify=left)
        ##label3.place(relx=.2, rely=.3)


        resizedframe = cv.resize(frame, (500, 500))
        cv.imwrite('tkimg.png', resizedframe)

        root = Tk()
        root.title("Вывод")
        root.geometry("1050x650")
        #root.geometry("800x800")

        # btns

        loadBtn = Button(text="Загрузить целевую сборку")
        updateBtn = Button(text="Обновить этап")
        updateBtn.bind('<Button-1>', Main().Process())


        #name= fd.askopenfilename() 
        #print(name)


        loadBtn.place(x=10, y=10)
        updateBtn.place(x=180, y=10)


        # label img

        img = Image.open("tkimg.png")
        render = ImageTk.PhotoImage(img)

        targetImg = Image.open("tkimgTarget.png")
        renderTarget = ImageTk.PhotoImage(targetImg)

        #labelImg0 = Label(root, image=render)
        #labelImg0.image = render
        #labelImg0.place(relx=.0, rely=.0)

        labelImg1 = Label(root, image=render)
        labelImg1.image = render
        labelImg1.place(relx=.0, rely=.2)

        labelImg2 = Label(root, image=renderTarget) 
        labelImg2.image = renderTarget
        labelImg2.place(relx=.5, rely=.2)

        
        # label text

        label0 = Label(text="Текущая сборка", justify=LEFT)
        label0.place(relx=.2, rely=.13)

        label1 = Label(text="Целевая сборка", justify=LEFT)
        label1.place(relx=.70, rely=.13)

        #label2 = Label(text="Графическая отладка", justify=LEFT)
        #label2.place(relx=.794, rely=.6)

        #label3 = Label(text="Текстовая отладка", justify=LEFT)
        #label3.place(relx=.2, rely=.3)

        #myText = '''
        #Не найдены элементы. Внесите элемент с кодом "1"
        #в поле зрения веб-камеры и нажмите кнопку "Обновить этап"
        #'''

        #label4 = Label(text=myText, justify=LEFT)
        #label4.place(relx=.3, rely=.3)



        # ghttps://ru.stackoverflow.com/questions/919894/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5-%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0-python-tkinter


        #root = Tk()
        #root.title('test')

        #notebook = ttk.Notebook(root, width=1000, height=700)
        #notebook.pack(fill='both', expand='yes')

        ##f1 = Text(root)
        ##f2 = Text(root)
        ##f3 = Text(root)

        ##nb.add(f1, text='page1')
        ##nb.add(f2, text='page2')
        ##nb.add(f3, text='page3')

        ## a_tab
        #a_tab = tk.Frame(notebook)

        #img = Image.open("tkimg.png")
        #render = ImageTk.PhotoImage(img)
        #labelImg0 = Label(root, image=render)


        ## b_tab
        #b_tab = tk.Frame(notebook)

        #notebook.add(a_tab, text="Сборки")
        #notebook.add(b_tab, text="Отладка")





        root.mainloop()


        # photo = ImageTk.PhotoImage(image = Image.fromarray(frame)) # преобразуем изобжаение из массива NumPy в PhotoImage
        # label = Label(image=photo)
        # label.image = photo # получили ссылку
        # label.pack()



        #!!!!! имеет место быть функции render