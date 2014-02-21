import cv2
import numpy

class PolygonFitting:
    
    def __init__(self):
        pass
    
    def findPolygon(self, image, originalimg):
        topFix = 770
        bottomFix = 790
        leftFix = 296
        rightFix = 306
        sideStep = 10
        top = topFix
        bottom = bottomFix
        left = leftFix
        right = rightFix
        points = numpy.array([[346,800]])
        ary = numpy.zeros((15, 10))
        image = cv2.cvtColor(image, cv2.cv.CV_GRAY2RGB)
        for y in range(0, 15):
            for x in range(0, 10):       
                #Waehle Bildbereich zum Betrachten aus
                roi = image[top:bottom,left:right]
                #Summiere alle Pixel in diesem Bereich: summe[0] = 0 entspricht alles schwarz
                summe = cv2.sumElems(roi)
                #print summe[0]
                if(summe[0]<=10.0):
                    cv2.rectangle(originalimg,(left,bottom),(right,top),(0,255,0),0) #rand
                    #points.append([bottom, right])
                    points = numpy.concatenate((points, ([[right-((right-left)/2),bottom-((bottom-top)/2)]])))
                    ary[y,x]=0
                else:
                    cv2.rectangle(originalimg,(left,bottom),(right,top),(0,0,255),-1) #gefuellt
                    ary[y,x]=1
                left = left + sideStep
                right = right + sideStep
            left = leftFix
            right = rightFix
            top = top - 20
            bottom = bottom - 20
          
        #cv2.imshow("Ohne Linie", originalimg)
        #pass
          
        top = topFix
        bottom = bottomFix
        left = leftFix
        right = rightFix
        center = 346
        centerTop = 346
        for y in range(0, 5):
            sumItemsLeft = 0
            sumItemsRight = 0
            found = False
            left = leftFix + (sideStep*5)
            right = rightFix + (sideStep*5)
            for x in range(5, 0,-1):
                if ary[y,x] == 1:
                    found = True
                if found == True:
                    ary[y,x]=1
                    sumItemsLeft += 1
                    cv2.rectangle(originalimg,(left,bottom),(right,top),(0,0,255),-1)
                left = left - sideStep
                right = right - sideStep
            found = False
            left = leftFix + (sideStep*5)
            right = rightFix + (sideStep*5)
            for x in range(5, 10):
                if ary[y,x] == 1:
                    found = True
                if found == True:
                    ary[y,x]=1
                    sumItemsRight += 1
                    cv2.rectangle(originalimg,(left,bottom),(right,top),(0,0,255),-1)
                left = left + sideStep
                right = right + sideStep
            left = leftFix
            right = rightFix
            top = top - 20
            bottom = bottom - 20
            centerTop += (sumItemsLeft - sumItemsRight) #/ 2
            if (y == 0):
                center = centerTop
        
              
        direction = cv2.fitLine(points, cv2.cv.CV_DIST_L1, 0, 0.01, 0.01)
        #cv2.line(originalimg, (346, 800), (346-(direction[0]*200), 800-numpy.abs(direction[1]*200)), (255,255,0),10)
        cv2.line(originalimg, (center, 800), (centerTop, 700), (255,255,0),10)
        cv2.imshow("Mit Linie", originalimg)
        
        return originalimg
        