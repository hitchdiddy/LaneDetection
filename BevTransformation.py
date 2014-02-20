import cv2
import numpy as np
from numpy import matrix
from cv2 import waitKey

class BevTransformation:

    amount = 300

    def __init__(self):
        pass
    
    def setAmount(self, val):
        self.amount = val
        
    def computeBev(self,image):      
        src = np.array([[350,131],[413,131],[75,325], [635,325]], np.float32)
        dst = np.array([[310,self.amount],[370,self.amount],[310,800], [370,800]], np.float32)
        #src = np.array([[348,251],[414,251],[224,316], [539,316]], np.float32)
        #dst = np.array([[310,50],[370,50],[310,800], [370,800]], np.float32)
        
        ret = cv2.getPerspectiveTransform(src, dst)
        
        newimg = cv2.warpPerspective(image, ret, (800,800))
        
        #cv2.imshow("test", newimg)
        #cv2.imwrite("/home/jan/Downloads/RoadSegmentation_Tutorial/300.jpg", newimg)
        
        #cv2.waitKey()
        
        
           
        
        return newimg
    
    def fitLine(self, image):
        
        return image
        
