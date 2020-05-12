import cv2 as cv
import numpy as np
import sys
import os
from Correct import *
import tensorflow as tf
from tensorflow import keras
from PIL import Image

def nothing(self):
    pass

class Recognition:

    def GetHsvMinMax(self, frame):
        cv.namedWindow( "result" ) # создаем главное окно
        cv.namedWindow( "settings" ) # создаем окно настроек

        # создаем 6 бегунков для настройки начального и конечного цвета фильтра
        cv.createTrackbar('h1', 'settings', 0, 255, nothing)
        cv.createTrackbar('s1', 'settings', 0, 255, nothing)
        cv.createTrackbar('v1', 'settings', 0, 255, nothing)
        cv.createTrackbar('h2', 'settings', 255, 255, nothing)
        cv.createTrackbar('s2', 'settings', 255, 255, nothing)
        cv.createTrackbar('v2', 'settings', 255, 255, nothing)
        cv.createTrackbar('default', 'settings', 0, 1, nothing)

        while True: 
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV )
            # считываем значения бегунков
            h1 = cv.getTrackbarPos('h1', 'settings')
            s1 = cv.getTrackbarPos('s1', 'settings')
            v1 = cv.getTrackbarPos('v1', 'settings')
            h2 = cv.getTrackbarPos('h2', 'settings')
            s2 = cv.getTrackbarPos('s2', 'settings')
            v2 = cv.getTrackbarPos('v2', 'settings')
            df = cv.getTrackbarPos('default', 'settings')
            if (df == 1):
                cv.destroyWindow("settings")
                cv.namedWindow( "settings" ) 
                cv.createTrackbar('h1', 'settings', 0, 255, nothing)
                cv.createTrackbar('s1', 'settings', 0, 255, nothing)
                cv.createTrackbar('v1', 'settings', 0, 255, nothing)
                cv.createTrackbar('h2', 'settings', 255, 255, nothing)
                cv.createTrackbar('s2', 'settings', 255, 255, nothing)
                cv.createTrackbar('v2', 'settings', 255, 255, nothing)
                cv.createTrackbar('default', 'settings', 0, 1, nothing)
        
            # формируем начальный и конечный цвет фильтра
            hsv_min = np.array((h1, s1, v1), np.uint8)
            hsv_max = np.array((h2, s2, v2), np.uint8)

            # накладываем фильтр на кадр в модели HSV
            thresh = cv.inRange(hsv, hsv_min, hsv_max)

            #показ изображения через несколько итераций, комп тупит
            #if count % 5 == 0:
            cv.imshow('result', thresh)

            # cap.release()
            print("hsv_min = np.array((",h1,", ",s1,", ",v1,"), np.uint8)")
            print("hsv_max = np.array((",h2,", ",s2,", ",v2,"), np.uint8)")
            # cv.destroyAllWindows()
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            #return 0


    def InsertColor(self):
        hsv_all = list()

        #красный
        # hsv_min = np.array(( 0 ,  171 ,  44 ), np.uint8)
        # hsv_max = np.array(( 178 ,  255 ,  255 ), np.uint8)
        # hsv_all.append(hsv_min)
        # hsv_all.append(hsv_max)

        #зеленый
        hsv_min = np.array(( 1 ,  0 ,  0 ), np.uint8)
        hsv_max = np.array(( 75 ,  255 ,  255 ), np.uint8)
        hsv_all.append(hsv_min)
        hsv_all.append(hsv_max)
        
        # hsv_min = np.array((0, 54, 5), np.uint8)
        # hsv_max = np.array((187, 255, 253), np.uint8)
        # hsv_all.append(hsv_min)
        # hsv_all.append(hsv_max)
        
        return hsv_all


    def GetRectangles(self, frame, hsv_all):
        hsv = cv.cvtColor( frame, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
        #проходим по всем hsv
        i = 0
        while i < len(hsv_all):
            hsv_min = hsv_all[i]
            hsv_max = hsv_all[i+1]
            i += 2
            # применяем цветовой фильтр
            thresh = cv.inRange( hsv, hsv_min, hsv_max )
            # ищем контуры и складируем их в переменную contours
            contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            # получаем вершины прямоугольников
            fullArrRects = list()
            for cnt in contours:
                rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
                area = int(rect[1][0]*rect[1][1]) # вычисление площади
                if area > 0:
                    arrRects = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
                    arrRects = np.int0(arrRects) # округление координат
                    fullArrRects.append(arrRects)

        # поиск координаты левого верхнего угла кубика
        arrTopLeftAngles = Correct().FindTopLeftAngle(fullArrRects)
        # массив, в котором перечисление начинается с верхней левой координаты
        sortedArrRects = Correct().SortArrRects(fullArrRects, arrTopLeftAngles)

        return sortedArrRects

    # def FindTopLeftAngle(self, arrRects):
    #     arrLenSidesRect = list()
    #     arrLenSidesRect = Correct().CalculateLenSides(arrRects)
    #     arrTopLeftAngle
    #     for rect in range(len(arrLenSidesRect)):
    #         for point in range(len(arrLenSidesRect[rect])):


    # def GetQR(self, frame, arrRects):
    #     neuralModel = tf.keras.models.load_model('emnist_digits.h5')
    #     # model.add (Flatten ())
    #     #получаем изображение области кубика
    #     for rect in range(len(arrRects)):
    #         firstPoint = 0
    #         endPoint = 2
    #         x = 0
    #         y = 1
    #         firstPointX = arrRects[rect][firstPoint][x]
    #         firstPointY = arrRects[rect][firstPoint][y]
    #         endPointX = arrRects[rect][endPoint][x]
    #         endPointY = arrRects[rect][endPoint][y]
    #         # cv.imshow("asdf"+str(rect), frame[firstPointY:endPointY, firstPointX:endPointX])
    #         # Считаем коэффициент соотношения сторон, что бы сохранить пропорции
    #         image = frame[firstPointY:endPointY, firstPointX:endPointX]
    #         # final_wide = 28
    #         # k = float(final_wide) / image.shape[1]
    #         # new_size = (final_wide, int(image.shape[0] * k))
    #         # уменьшаем изображение до подготовленных размеров
    #         resized = cv.resize(image, (28, 28), interpolation=cv.INTER_AREA)
    #         cv.imshow("Resize image"+str(rect), resized)
    #         #конвертировать в np.array
    #         # miniFrame = np.array(resized)
    #         # miniFrame = cv.imread('1111.png')
    #         # mf = image.reshape(image.shape[0], 28, 28, 1)
    #         # print(miniFrame.shape)
    #         # predictions = neuralModel.predict(resized)
    #         break

    #     # return np.array(resized)


    def GetQR(self, frame, arrRects):
            neuralModel = tf.keras.models.load_model('emnist_digits.h5')
            # model.add (Flatten ())
            #получаем изображение области кубика
            for rect in range(len(arrRects)):
                firstPoint = 0
                endPoint = 2
                x = 0
                y = 1
                firstPointX = arrRects[rect][firstPoint][x]
                firstPointY = arrRects[rect][firstPoint][y]
                endPointX = arrRects[rect][endPoint][x]
                endPointY = arrRects[rect][endPoint][y]

                testFrame = frame[firstPointY:endPointY, firstPointX:endPointX]

                #перевести в hsv и регулировать уже насыщенности/яркости искать черный тупо)

                # формируем начальный и конечный цвет фильтра
                hsv_min = np.array(( 0 ,  0 ,  0 ), np.uint8)
                hsv_max = np.array(( 255 ,  0 ,  0 ), np.uint8)

                # накладываем фильтр на кадр в модели HSV
                img = cv.inRange(testFrame, hsv_min, hsv_max)

                # меняем размер
                finded_h = (28 * 100) / img.shape[0]
                finded_w = (28 * 100) / img.shape[1]

                scale_percent = finded_h # percent of original size
                width = int(img.shape[1] * scale_percent / 100)
                height = int(img.shape[0] * scale_percent / 100)
                dim = (width, height)

                img = cv.resize(img, dim, interpolation = cv.INTER_AREA)


                cv.imwrite('buff.png', img)


                i = Image.open('buff.png')
                pixels = i.load() 
                width, height = i.size

                count = 0
                all_pixels = []


                if height == 28 and width == 28:
                    all_pixels = []
                    for x in range(width):
                        for y in range(height):
                            if pixels[y, x] == 0:
                                cpixel = pixels[y, x]
                                all_pixels.append(cpixel)
                            else:
                                all_pixels.append(255)
                
                    print("ALLLLLLLLL")
                    print(len(all_pixels))



                if width != 28:

                    if width < 28:

                        delta = 28 - width
                        for x in range(28):
                            for y in range(28):
                                if y < width:
                                    if pixels[y, x] == 0:
                                        all_pixels.append(pixels[y, x])
                                    elif pixels[y, x] != 0:
                                        all_pixels.append(255)
                                elif y == width:
                                    for px in range(delta):
                                        all_pixels.append(0)

                        print("WIDTH small")
                        print(len(all_pixels))



                    if width > 28:

                        # думаю будет лучше дельту делить пополам и добавлять слева от картинки половину столбцов и половину справа
                        delta = width - 28
                        for x in range(height):
                            for y in range(width):
                                if y < 28:
                                    if pixels[y, x] == 0:
                                        all_pixels.append(pixels[y, x])
                                    elif pixels[y, x] != 0:
                                        all_pixels.append(255)
                                elif y > 28 and y < width:
                                    pass

                        print("WIDTH big")
                        print(len(all_pixels))


                if height != 28:

                    if height < 28:
                        for y in range(heigth):
                            for x in range(width):
                                all_pixels.append(pixels[x, y])

                        delta = 28 - height
                        for i in range(delta * 28):
                            all_pixels.append(0)
                        
                        print("HEIGTH")
                        print(len(all_pixels))


                    if height > 28:
                        for y in range(heigth):
                            for x in range(width):
                                all_pixels.append(pixels[x, y])

                        delta = 28 - height
                        for i in range(delta * 28):
                            all_pixels.append(0)
                        
                        print("HEIGTH")
                        print(len(all_pixels))



                buff = list()
                arr = list()
                count = 0

                for i in all_pixels:
                    count += 1
                    buff.append(i)
                    if count == 28:
                        arr.append(buff[-28:])
                        count = 0

                np_array = np.asarray(arr)

                img = Image.fromarray(np_array)

                img.show()





                        #for x in range(27):
                        #    for y in range(27):
                        #        print(pixels[y, x])

                        #for i in range(width*height):
                        #    count += 1
                        #    if count == width:
                        #        for j in range(28 - width):
                        #            all_pixels.append(0)
                        #            count = 0
                        #    if pixels[y, x] == 0:
                        #        all_pixels.append(pixels[y, x])
                        #    if pixels[y, x] != 0:
                        #        all_pixels.append(255)
                        #print(all_pixels)




                        #all_pixels = []
                        #for i in range(width*height):
                        #    count += 1
                        #    if count == width:
                        #        for j in range(28 - width):
                        #            #all_pixels.append(0)
                        #            count = 0
                        #    if pixels[y, x] == 0:
                        #        cpixel = pixels[y, x]
                        #        all_pixels.append(cpixel)
                        #    else:
                        #        all_pixels.append(255)
                        #print(all_pixels)
                    
                        #buff = list()
                        #arr = list()
                        #count = 0




                        #for i in all_pixels:
                        #    count += 1
                        #    buff.append(i)
                        #    if count == 28:
                        #        arr.append(buff[-28:])
                        #        count = 0
                        #print(arr)
                        #np_array = np.asarray(arr)

                        #img = Image.fromarray(np_array)



                        #img.show()
                    



                    #img1 = cv.imread('bg.png')
                    #img2 = cv.imread('buff.png')

                    #brows, bcols = img1.shape[:2]
                    #rows,cols,channels = img2.shape
                    ## Ниже я изменил roi, чтобы картинка выводилась посередине, а не в левом верхнем углу
                    ##roi = img1[int(brows/2)-int(rows/2):int(brows/2)+int(rows/2), int(bcols/2)- 
                    ##int(cols/2):int(bcols/2)+int(cols/2) ]
                    #roi = img1[0:rows, 0:cols]


                    #img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
                    #ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
                    #mask_inv = cv.bitwise_not(mask)

                    #img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

                    #img2_fg = cv.bitwise_and(img2,img2,mask = mask)

                    #dst = cv.add(img1_bg,img2_fg)
                    #img1[int(brows/2)-int(rows/2):int(brows/2)+int(rows/2), int(bcols/2)- 
                    #int(cols/2):int(bcols/2)+int(cols/2) ] = dst
                    #cv.imwrite('res.png',img1)


                #else:
                #    i = Image.open('buff.png')


                #pixels = i.load() 
                #width, height = i.size

                #all_pixels = []
                #for x in range(width):
                #    for y in range(height):
                #        if pixels[y, x] == 0:
                #            cpixel = pixels[y, x]
                #            all_pixels.append(cpixel)
                #        else:
                #            all_pixels.append(255)
                

                #buff = list()
                #arr = list()
                #count = 0


                #for i in all_pixels:
                #    count += 1
                #    buff.append(i)
                #    if count == 28:
                #        arr.append(buff[-28:])
                #        count = 0

                #np_array = np.asarray(arr)

                #img = Image.fromarray(np_array)



                im2arr = np.array(img)
                im2arr = im2arr/255
                im2arr = im2arr.reshape(1, 28, 28)
                pred = neuralModel.predict(im2arr)
                print(pred)
                print(np.argmax(pred[0]))



                    
                break

                # на выходе должно быть : массив координат + qr код кубика с этими координатами

            # return np.array(resized)


