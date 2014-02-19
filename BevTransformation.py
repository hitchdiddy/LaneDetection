import cv2
import numpy as np
from numpy import matrix
from cv2 import waitKey

class BevTransformation:

    def __init__(self):
        pass
        
    def computeBev(self,image, value):
        y = 0 #Hoehe
        #Calibration data
        trans = matrix([[0.064204210331161901], [-1.1659632805953182],[ 1.9516283622638129]])
        R  = matrix([[1.0003006126397809, 0.0027500404928677445, 0.0076948745820731171],[-0.0029378803282461181, 1.0000292823888794, 0.024511264068503628],[-0.007625134538036143, -0.024533048818819892, 1.000003988608658]])
        T  = matrix([[1,0,0, trans[0]],[0,1,0,trans[1]],[0,0,1,trans[2]],[0,0,0,1]]) 
        
        #Image data
        t_u = 4.4/1000000.0*1600/800 #horizontal size of 1 pixel
        t_v = 4.4/1000000.0*1200/600 #vertical size of 1 pixel
        
        f = matrix([[459 * 2 * t_v],[459 * t_u]]) #f=[fx, fy] im mm
        f_px = matrix([[918],[918]])
        center = matrix([[185.2133],[142.4146]])
        u_0 = center[0] * 2
        v_0 = center[1] * 2
        
        #BEV data
        res = 1
        xBounds = matrix([[-10],[10]])
        zBounds = matrix([[0],[50]])
        
        #Metrische Koordinatesystem
        zVec = range(zBounds[0],zBounds[1],res)
        xVec = range(xBounds[0],xBounds[1],res)
        
        
        
        
        
        
        
        
        if(value < 0 or value > 400):
            value = 300
        
        
        src = np.array([[350,131],[413,131],[75,325], [635,325]], np.float32)
        dst = np.array([[310,value],[370,value],[310,800], [370,800]], np.float32)
        
        ret = cv2.getPerspectiveTransform(src, dst)
        
        newimg = cv2.warpPerspective(image, ret, (800,800))
        
        cv2.imshow("test", newimg)
        #cv2.imwrite("/home/jan/Downloads/RoadSegmentation_Tutorial/300.jpg", newimg)
        
        #cv2.waitKey()
        
        
           
        
        return newimg
        
