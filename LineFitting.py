import cv2
import numpy as np
import math

class LineFitting:


    
    #dataBlack = ""
    def __init__(self):
        self.rho = 1
        self.theta = np.pi/180
        self.threshold = 60
        self.minLength = 100
        self.patchsizex = 400
        self.patchsizey = 200
        #self.dataBlack = dataBlack
        pass
    def setRho(self,rho1):
        self.rho = rho1
    def setTheta(self,theta1):
        self.theta = theta1
    def setThreshold(self,threshold1):
        self.threshold = threshold1
    def setMinLength(self,minLength1):
        
        self.minLength = minLength1*min(self.patchsizex,self.patchsizey)/100.0
        return self.minLength
      
    """def drawLine(self,rho,theta,img,dx,dy):
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a*rho
        y0 = b*rho;
        x1 = int(x0 + 1000*(-b));
        y1 = int(y0 + 1000*(a));
        x2 = int(x0 - 1000*(-b));
        y2 = int(y0 - 1000*(a));
        cv2.line(img, (dx+x1,dy+y1), (dx+x2,dy+y2), (255,0,0)) """
        
           
        
    def findLine(self,image):
        imageBlack = np.zeros((800,800),np.uint8)
        i = 0
        listVectors = []
        height, width= image.shape
        #image2 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for y in range(0, int(height/self.patchsizey)):
            for x in range(0, int(width/self.patchsizex)):
                subimg = image[(x*self.patchsizex):(x*self.patchsizex+self.patchsizex),(y*self.patchsizey):(y*self.patchsizey+self.patchsizey)]
                imageBlack = self.findInPatch(subimg,imageBlack,x,y)
                """vector = cv2.HoughLines(subimg, self.rho, self.theta, self.threshold)
                if(vector!=None):
                    print(vector)
                    self.drawLine(vector[0][0][0], vector[0][0][1], image, x*self.patchsizex,y*self.patchsizey)
                    
                    #listVectors.append(vector)"""
        
        return imageBlack #listVectors.pop()
    
    def findInPatch(self,subimg, imageBlack,x,y):
        vector = None
        vector = cv2.HoughLinesP(subimg,self.rho, self.theta, self.threshold, vector,self.minLength)
        if(vector!=None):
            end = (vector.size/4)-1
            #for i2 in range(0,end):
            i2 = 0
            for x1,y1,x2,y2 in vector[i2]:
                    #cv2.imshow('test3', subimg)
                    cv2.line(imageBlack,(y*self.patchsizey+x1,x*self.patchsizex+y1),(y*self.patchsizey+x2,x*self.patchsizex+y2),(255,255,255),2)
        return imageBlack
    
if __name__ == '__main__':
    
    
    line = LineFitting()
    
    
    cv2.namedWindow('edge')
    #cv2.createTrackbar('thrs1', 'edge', 2000, 10000, nothing)
    #cv2.createTrackbar('thrs2', 'edge', 3000, 10000, nothing)
    #cv2.createTrackbar('thrs3', 'edge', 0, 10, nothing)
  
    
    
    #print("Testfunction for Edge-Detection")
    subimg = cv2.imread('test1.png')
    subimg = cv2.cvtColor(subimg, cv2.cv.CV_BGR2GRAY)
    imageBlack = np.zeros((400,400),np.uint8)
    line.findInPatch(subimg, imageBlack,0,0)
    cv2.imshow('', imageBlack)
    cv2.imshow('2', subimg)
    cv2.waitKey(0)
    pass
"""
    
    while True:
        edgeDet.minTresh = cv2.getTrackbarPos('thrs1', 'edge')
        edgeDet.maxTresh = cv2.getTrackbarPos('thrs2', 'edge')
        edgeDet.sobel = cv2.getTrackbarPos('thrs3', 'edge')
        edge = edgeDet.computeEdges(img)
        vis = edge.copy()
        vis /= 2
     
        cv2.imshow('edge', vis)
        ch = cv2.waitKey(5)
        if ch==27:
            break
      
    cv2.destroyAllWindows()"""