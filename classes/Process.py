
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
    

        