import cv2
import numpy as np
import math

class LineFitting:
    patchsizex = 50
    patchsizey = 200
    rho = 1
    theta = np.pi/180
    threshold = 60
    def __init__(self):
        self.rho = 1
        self.theta = np.pi/180
        self.threshold = 60
        pass
    def setRho(self,rho1):
        self.rho = rho1
    def setTheta(self,theta1):
        self.theta = theta1
    def setThreshold(self,threshold1):
        self.threshold = threshold1
      
    def drawLine(self,rho,theta,img,dx,dy):
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a*rho
        y0 = b*rho;
        x1 = int(x0 + 1000*(-b));
        y1 = int(y0 + 1000*(a));
        x2 = int(x0 - 1000*(-b));
        y2 = int(y0 - 1000*(a));
        cv2.line(img, (dx+x1,dy+y1), (dx+x2,dy+y2), (255,0,0))    
        
    def findLine(self,image):
        i = 0
        listVectors = []
        height, width= image.shape
        #image2 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for y in range(0, int(height/self.patchsizey/2)-1):
            for x in range(0, int(width/self.patchsizex/2)-1):
                subimg = image[(x*self.patchsizex):(x*self.patchsizex+self.patchsizex),(y*self.patchsizey):(y*self.patchsizey+self.patchsizey)]
                vector = cv2.HoughLines(subimg, self.rho, self.theta, self.threshold)
                if(vector!=None):
                    print(vector)
                    self.drawLine(vector[0][0][0], vector[0][0][1], image, x*self.patchsizex/2,y*self.patchsizey/2)
                    
                    #listVectors.append(vector)
        
        return image #listVectors.pop()
    