import cv2
import numpy as np
from matplotlib import pyplot as plt



class EdgeDetection:

    minTresh = 2000
    maxTresh = 3000

    def __init__(self):
        self.minTresh = 2000
        self.maxTresh = 3000
        pass
        
    def computeEdges(self,image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray_image, self.minTresh, self.maxTresh, apertureSize=5)
    
    
    
    def setMinTresh(self, val):
        self.minTresh = val
    def setMaxTresh(self, val):
        self.maxTresh = val
     
    
    
    def main(self):
        print("hello")
   
   
def nothing(*arg):
    pass  
     
if __name__ == '__main__':
    
    
    edgeDet = EdgeDetection()
    
    
    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 2000, 10000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 2000, 10000, nothing)
  
    
    
    print("Testfunction for Edge-Detection")
    img = cv2.imread('../messi.jpg',0)

    
    while True:
        edgeDet.minTresh = cv2.getTrackbarPos('thrs1', 'edge')
        edgeDet.maxTresh = cv2.getTrackbarPos('thrs2', 'edge')
        edge = edgeDet.computeEdges(img)
        vis = edge.copy()
        vis /= 2
     
        cv2.imshow('edge', vis)
        ch = cv2.waitKey(5)
        if ch==27:
            break
      
    cv2.destroyAllWindows()
    
    
 
