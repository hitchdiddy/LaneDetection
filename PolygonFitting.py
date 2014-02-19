import cv2

class PolygonFitting:
    
    def __init__(self):
        pass
    
    def findPolygon(self, image):
         #Waehle Bildbereich zum Betrachten aus
        image = cv2.cvtColor(image, cv2.cv.CV_GRAY2RGB)
        roi = image[760:800,326:366]
        #Summiere alle Pixel in diesem Bereich: summe[0] = 0 entspricht alles schwarz
        summe = cv2.sumElems(roi)
        print summe[0]
        if(summe[0]<=0.0):
            cv2.rectangle(image,(326,800),(366,780),(0,255,0),3)
        else:
            cv2.rectangle(image,(326,800),(366,780),(0,0,255),-1)  
        cv2.imshow("", image)
        pass
        