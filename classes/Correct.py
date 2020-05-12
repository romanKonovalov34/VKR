import cv2 as cv
import numpy as np
import os
import sys
import math
from math import fabs

class Correct: 
    def ModifyArrRects(self, arrRects):
        arrPoints = list()
        for rect in range(len(arrRects)):
            for point in range(len(arrRects[rect])):
                arrPoints.append(arrRects[rect][point])
        return arrPoints #массив точек


    # def NewBox(self, arrRects):
    #     for rect in range(len(arrRects)):
    #         for pointI in range(len(arrRects[rect])):
    #         #     for pointJ in range(len(arrRects[rect])):
    #         #         if pointI[0] == pointJ[0]:
    #         #             print("yes")
    #         #             break
    #             print(arrRects[rect][pointI])

    # можно сделать функцию на проверку 90 градусов одного из кубиков
    # def RectIs90 МОЖНО ДОДЕЛАТЬ И ПРОВЕРИТЬ НА ПРОВЕРКУ ПАРАЛЛЕЛЬНОСТИ (ХОТЯ Я ДУМАЮ ЭТО НЕ НАДО)
        # selectedRect = list()
        # for rect in range(len(arrRects)):
        #     selectedRect.append(arrRects[rect])
        #     # print(selectedRect[-1])
        #     lenSides = list()
        #     for point in range(len(selectedRect[-1])):
        #         # print(selectedRect[-1][point])
        #         x = selectedRect[-1][point][0]
        #         y = selectedRect[-1][point][1]
        #         # print(x)
        #         if point+1 < len(selectedRect[-1]):
        #             # print(selectedRect[rect][point+1])
        #             xNext = selectedRect[rect][point+1][0]
        #             yNext = selectedRect[rect][point+1][1]
        #             if x == xNext:
        #                 print(x)

    #в идеале каждый кубик параллелен последующему (это надо учитывать qr код)
    # def IsParallelVertical(self, frame, box):
    #     for i in range(len(box)):
    #         for j in range(len(box[i])):
    #             for k in range(len(box[i])):
    #                 if box[i][j][0] == box[i][k][0]: #с помощью точек можно найти линии и определить, параллельны ли они
    #                     print("yes")
    #                     # break


    # def FindDistance(self, box):
    #      for i in range(len(box)):
    #         for j in range(len(box[i])):
    #             for k in range(len(box[i])):
    #                 #находим координату (x) каждой вертикальной грани прямоугольника
    #                 xj = box[i][j][0]
    #                 xk = box[i][k][0]
    #                 #
    #                 if xj == xk:
    #                     print("yes")
    #                     break

    #проверка находятся ли все кубики в одной плоскости (у них все стороны должны быть равны ±)
    # def IsSamePlane(self, arrPoints):
    #     for i in range(len(arrPoints)):
    #         print(arrPoints[i])

    def FindTopLeftAngle(self, arrRects):
        #споиск координаты левого верхнего угла каждого кубика
        #координата по x определенно должна быть меньше двух других координат по x (с координтой y точно так же)
        arrTopLeftAngles = list()
        for rect in range(len(arrRects)):
            minX = 100000
            minY = 100000
            for pointI in range(len(arrRects[rect])):
                for pointJ in range(len(arrRects[rect])):
                    #если выбранный элемент X меньше следующего
                    if arrRects[rect][pointI][0] < arrRects[rect][pointJ][0] and arrRects[rect][pointI][0] < minX:
                        minX = arrRects[rect][pointI][0]
                        # minX = 
                    #если следующий элемент X меньше выбранного
                    elif arrRects[rect][pointI][0] > arrRects[rect][pointJ][0] and arrRects[rect][pointJ][0] < minX:
                        minX = arrRects[rect][pointJ][0]
                    #если выбранный элемент Y меньше следующего
                    if arrRects[rect][pointI][1] < arrRects[rect][pointJ][1] and arrRects[rect][pointI][1] < minY:
                        minY = arrRects[rect][pointI][1]
                    #если следующий элемент Y меньше выбранного
                    elif arrRects[rect][pointI][1] > arrRects[rect][pointJ][1] and arrRects[rect][pointJ][1] < minY:
                        minY = arrRects[rect][pointJ][1]
            arrTopLeftAngles.append([minX, minY])
        return arrTopLeftAngles


    def SortArrRects(self, arrRects, arrTopLeftAngles):
        idPoint = 0
        arrPoint = list()
        sortedArrRects = list()
        for rect in range(len(arrRects)):
            xTopLeft = arrTopLeftAngles[rect][0]
            yTopLeft = arrTopLeftAngles[rect][1]
            for point in range(len(arrRects[rect])):
                x = arrRects[rect][point][0]
                y = arrRects[rect][point][1]
                if x == xTopLeft and y == yTopLeft:
                    #нашли индекс этого угла в прямоугольнике
                    idPoint = point
                    break
            #добавляем все точки от найденной точки и до последней в изначальном массиве
            for point in range(idPoint, len(arrRects[rect][3])+2):
                arrPoint.append(arrRects[rect][point])
            #добавляем последние точки (от последней точки в массиве до найденной верхней левой точки)
            for point in range(idPoint):
                arrPoint.append(arrRects[rect][point])

            sortedArrRects.append(arrPoint[-4:])
        return np.array(sortedArrRects)


#найти длину сторон всех кубиков
    def CalculateLenSides(self, arrRects):
        selectedRect = list()
        # lenSides = list()
        resLenSides = list()
        for rect in range(len(arrRects)):
            selectedRect.append(arrRects[rect])
            # print(selectedRect[-1])
            lenSides = list()
            for point in range(len(selectedRect[-1])):
                # print(selectedRect[-1][point])
                x = selectedRect[-1][point][0]
                y = selectedRect[-1][point][1]
                # print(x)
                if point+1 < len(selectedRect[-1]):
                    # print(selectedRect[rect][point+1])
                    xNext = selectedRect[-1][point+1][0]
                    yNext = selectedRect[-1][point+1][1]
                    if x == xNext:
                        deltaY = y - yNext                            
                        # print(y, "-", yNext, "==", int(fabs(deltaY)))
                        lenSides.append(int(fabs(deltaY)))
                    if y == yNext:
                        deltaX = x - xNext
                        # print(x, "-", xNext, "==", int(fabs(deltaX)))
                        lenSides.append(int(fabs(deltaX)))
                    #проверяем длину от последней точки до первой
                    if point+1 == (len(selectedRect[-1]))-1:
                        x = selectedRect[-1][0][0]
                        y = selectedRect[-1][0][1]
                        xNext = selectedRect[-1][point+1][0]
                        yNext = selectedRect[-1][point+1][1]
                        if x == xNext:
                            deltaY = y - yNext                            
                            # print(y, "-", yNext, "==", int(fabs(deltaY)))
                            lenSides.append(int(fabs(deltaY)))
                        if y == yNext:
                            deltaX = x - xNext
                            # print(x, "-", xNext, "==", int(fabs(deltaX)))
                            lenSides.append(int(fabs(deltaX)))
            resLenSides.append(lenSides)
        return resLenSides

    #проверка находятся ли все кубики в одной плоскости (результат == у них все стороны должны быть равны ± 5)
    def IsSamePlane(self, arrRects):
        lenSides = list()
        deltaInterval = list()
        flag = True
        failList = list()
        arrLenSidesRect = self.CalculateLenSides(arrRects)
        for rect in range(len(arrLenSidesRect)):
            for side in range(len(arrLenSidesRect[rect])):
                for nextSide in range(len(arrLenSidesRect[rect])):
                    nextSideIntervalMin = arrLenSidesRect[rect][nextSide]-35
                    nextSideIntervalMax = arrLenSidesRect[rect][nextSide]+35
                    if flag == False:
                        failList.append(rect)
                        print("Кубик", rect, "не параллелен другим")
                    flag = False
                    for value in range(nextSideIntervalMin, nextSideIntervalMax):
                        if arrLenSidesRect[rect][side] == value:
                            print("Yes")
                            flag = True
                            break
                #потому что надо сравнить только одну сторону каждого кубика со всеми другими его сторонами
                break

def TeoremPif(deltaX, deltaY):
	length = int(math.sqrt(deltaX**2 + deltaY**2))
	return length

def FindLength(arrRects):
	x0 = 0
	y0 = 0
	x1 = 0
	y1 = 0
	deltaX = 0
	deltaY = 0
	arrLength = list()
	for rect in range(len(arrRects)):
		if rect+1 < len(arrRects):
			x0 = arrRects[rect][0][0]
			y0 = arrRects[rect][0][1]
			x1 = arrRects[rect+1][0][0]
			y1 = arrRects[rect+1][0][1]
			deltaX = abs(x0 - x1)
			delatY = abs(y0 - y1)
			if deltaX < 10:
				arrLength.append(deltaY)
				#break
			elif deltaY < 10:
				arrLength.append(deltaX)
				#break
			else:
				length = TeoremPif(deltaX, deltaY)
				arrLength.append(length) #длин будет всегда на 1 меньше кол-ва кубиков
	return arrLength
    
# def main():
# 	lastCountRects = 1
# 	arrRects = list()
# 	arrRects = [ [ [10,10], [20,10], [20,20], [10,20] ],
# 				 [ [30,10], [40,10], [40,20], [30,20] ],
# 				 [ [40,10], [50,10], [40,20], [50,20] ] ]

# 	if len(arrRects) > 1 and len(arrRects) > lastCountRects:
# 		arrLength = FindLength(arrRects)
# 		print(arrLength)	
# 		lastCountRects = len(arrRects)

# main()


    

    # def IsSamePlane(self, arrRects):
    #     lenSides = list()
    #     for rect in range(len(arrRects)):
    #         for point in range(len(arrRects[rect])):
    #             x = arrRects[rect][point][0]
    #             y = arrRects[rect][point][1]
    #             if point+1 < len(arrRects[rect]):
    #                 xNext = arrRects[rect][point+1][0]
    #                 yNext = arrRects[rect][point+1][1]
    #                 if x == xNext:
    #                     print(x)