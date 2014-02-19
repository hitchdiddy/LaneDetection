from numpy import matrix

class BevTransformation:

    def __init__(self):
        pass
        
    def computeBev(self,image):
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
        res = 0.1
        xBounds = matrix([[-10],[10]])
        yBounds = matrix([[0],[50]])
           
        
        return image
        
