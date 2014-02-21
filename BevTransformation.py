import cv2
import numpy as np

class BevTransformation:

    amount = 300
    #Coordinates of four points in the perspective image      
    src = np.array([[350,131],[413,131],[75,325], [635,325]], np.float32)
    #Coordinates of the same four points in the metric image
    dst = np.array([[310,300],[370,300],[310,800], [370,800]], np.float32)

    def __init__(self):
        pass
    
    def setAmount(self, val):
        #self.amount = val
        pass
        
    def computeBev(self,image):
        #src = np.array([[348,251],[414,251],[224,316], [539,316]], np.float32)
        #dst = np.array([[310,50],[370,50],[310,800], [370,800]], np.float32)
        
        #Calculate the transform matrice
        ret = cv2.getPerspectiveTransform(self.src, self.dst)
        
        #transform the image
        newimg = cv2.warpPerspective(image, ret, (800,800))
        
        #cv2.imshow("test", newimg)
        #cv2.imwrite("/home/jan/Downloads/RoadSegmentation_Tutorial/300.jpg", newimg)
        
        #cv2.waitKey()
                   
        
        return newimg
    
    def computePers(self, image):
        #Calculate the transform matrice backwards
        ret = cv2.getPerspectiveTransform(self.src, self.dst)
        
        #transform the image
        newimg = cv2.warpPerspective(image, ret, (800,800),flags=cv2.WARP_INVERSE_MAP)
        newimg = newimg[120:320,0:800]
        #cv2.imshow("test2", newimg)
        return newimg
    
    def fitLine(self, image):
        
        return image
        
