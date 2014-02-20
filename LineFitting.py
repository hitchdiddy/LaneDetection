import cv2
import numpy as np

class LineFitting:
    patchsizex = 50
    patchsizey = 200
    rho = 1
    theta = np.pi/180
    threshold = 100
    def __init__(self):
        pass
    def setRho(self,rho1):
        self.rho = rho1
    def setTheta(self,theta1):
        self.theta = theta1
    def setThreshold(self,threshold1):
        self.threshold = threshold1
        
    def findLine(self,image):
        i = 0
        listVectors = []
        height, width= image.shape
        #image2 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for y in range(0, int(height/self.patchsizex/2)-1):
            for x in range(0, int(width/self.patchsizey/2)-1):
                subimg = image[(x*self.patchsizex):(x*self.patchsizex+self.patchsizex),(y*self.patchsizey):(y*self.patchsizey+self.patchsizey)]
                #vector = cv2.HoughLines(subimg, self.rho, self.theta, self.threshold)
                #listVectors.append(vector)
        
        return image #listVectors.pop()
    