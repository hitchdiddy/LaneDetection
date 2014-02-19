import cv2

class PolygonFitting:
    
    def __init__(self):
        pass
    
    def findPolygon(self, image):
        
        top = 780
        bottom = 800
        left = 226
        right = 246
        image = cv2.cvtColor(image, cv2.cv.CV_GRAY2RGB)
        for x in range(0, 13):        
            for y in range(0, 10):
                #Waehle Bildbereich zum Betrachten aus
                roi = image[top:bottom,left:right]
                #Summiere alle Pixel in diesem Bereich: summe[0] = 0 entspricht alles schwarz
                summe = cv2.sumElems(roi)
                print summe[0]
                if(summe[0]<=20.0):
                    cv2.rectangle(image,(left,bottom),(right,top),(0,255,0),1) #rand
                else:
                    cv2.rectangle(image,(left,bottom),(right,top),(0,0,255),-1) #gefuellt
                top = top - 40
                bottom = bottom - 40
            bottom = 800
            top = 780
            left = left + 20
            right = right + 20
          
        cv2.imshow("", image)
        pass
        