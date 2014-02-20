import cv2
import numpy

class PolygonFitting:
    
    def __init__(self):
        pass
    
    def findPolygon(self, image, originalimg):
        
        top = 780
        bottom = 800
        left = 296
        right = 306
        points = numpy.array([[346,800],[346,0]])
        xSum = 0;
        ySum = 0;
        pointCount = 0;
        image = cv2.cvtColor(image, cv2.cv.CV_GRAY2RGB)
        for x in range(0, 11):        
            for y in range(0, 20):
                #Waehle Bildbereich zum Betrachten aus
                roi = image[top:bottom,left:right]
                #Summiere alle Pixel in diesem Bereich: summe[0] = 0 entspricht alles schwarz
                summe = cv2.sumElems(roi)
                #print summe[0]
                if(summe[0]<=20.0):
                    cv2.rectangle(originalimg,(left,bottom),(right,top),(0,255,0),0) #rand
                    #points.append([bottom, right])
                    points = numpy.concatenate((points, ([[right-((right-left)/2),bottom-((bottom-top)/2)]])))
                    xSum += right-((right-left)/2)
                    ySum += bottom-((bottom-top)/2)
                    pointCount += 1
                else:
                    cv2.rectangle(originalimg,(left,bottom),(right,top),(0,0,255),-1) #gefuellt
                top = top - 20
                bottom = bottom - 20
            bottom = 800
            top = 780
            left = left + 10
            right = right + 10
          
        cv2.imshow("Ohne Linie", originalimg)
        #pass
        
        cv2.circle(originalimg, (xSum/pointCount,ySum/pointCount),5,(128,0,0))
        
        direction = cv2.fitLine(points,6, 0, 1, 0.01)
        #cv2.line(originalimg, direction)
        #cv2.line(originalimg, (direction[2], direction[3]), (direction[2]+direction[0], direction[3]+direction[1]), (255,255,0),10)
        #for x in range(0, points.size/2-1):
            #ptOne = tuple(points[x])#(points[x,0], points[x,1])
            #ptTwo = tuple(points[x+1])#(points[x+1,0], points[x+1,1])
            #cv2.line(originalimg, ptOne, ptTwo, (0,0,255),1)
        cv2.imshow("Mit Linie", originalimg)
        
        return originalimg
        