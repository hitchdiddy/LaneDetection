import cv2
import numpy as np
#from matplotlib import pyplot as plt



class EdgeDetection:

    minTresh = 2000
    maxTresh = 3000
    sobel = 0

    def __init__(self):
        self.minTresh = 2000
        self.maxTresh = 3000
        self.sobel = 0
        pass
        
    def computeEdges(self,image):
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #image = cv2.Sobel(image,cv2.CV_16S,self.minTresh,self.maxTresh,ksize=5)
        #image = cv2.Canny(image, self.minTresh, self.maxTresh, apertureSize=5)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        image = cv2.Canny(image, self.minTresh, self.maxTresh, apertureSize=5)
        
        image = cv2.Sobel(image,cv2.CV_8U,self.sobel+1,0,ksize=5)
        
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        return image
    
    
    
    def setMinTresh(self, val):
        self.minTresh = val
    def setMaxTresh(self, val):
        self.maxTresh = val
    def setSobel(self, val):
        self.sobel = val     
    
    
    def main(self):
        print("hello")
   
   
def nothing(*arg):
    pass  
     
if __name__ == '__main__':
    
    
    edgeDet = EdgeDetection()
    
    
    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 2000, 10000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 3000, 10000, nothing)
    cv2.createTrackbar('thrs3', 'edge', 0, 10, nothing)
  
    
    
    print("Testfunction for Edge-Detection")
    img = cv2.imread('../messi.jpg')

    
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
      
    cv2.destroyAllWindows()
    
    
 
