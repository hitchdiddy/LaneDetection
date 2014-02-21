import cv2
import numpy as np
import os
import sys
import glob
import math
from BevTransformation import BevTransformation
from LineFitting import LineFitting
from EdgeDetection import EdgeDetection
from PolygonFitting import PolygonFitting
from PyQt4 import QtCore, QtGui 

from PyQt4.QtCore import QPoint, QTimer
from PyQt4.QtGui import QApplication, QImage, QWidget



def processImage(filename):

    cv2.waitKey()

    #print 'processing'
    image = cv2.imread(filename)
        
    # Load current ground truth
    #cur_groundTruth = cv2.imread(self.gt_Data_files[i], cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)
    # GT -> binary map
    #cur_groundTruth = cur_groundTruth > 0;
    
    
    #flag, out = cv2.threshold(image, 104, 255, cv2.THRESH_BINARY)
    
    out = image
        
    ## 1) Feature Extraction
    # Extract color channels
    # NOTE: OpenCV has BGR ordering
    r_channel = image[:, :, 2]
    g_channel = image[:, :, 1]
    b_channel = image[:, :, 0]
        

    return out





def convertIpl(cvBGRImg):
    #BGR2RGB
    cvRGBImg = cv2.cvtColor(cvBGRImg, cv2.cv.CV_BGR2RGB)
    
    #convert numpy mat to pixmap image
    qimg = QtGui.QImage(cvRGBImg.data,cvRGBImg.shape[1], cvRGBImg.shape[0], QtGui.QImage.Format_RGB888)
    
    #return qimg

    qpm = QtGui.QPixmap.fromImage(qimg)    

    return qpm

def convertIplG(cvBGRImg):
    #BGR2RGB
    cvRGBImg = cv2.cvtColor(cvBGRImg, cv2.cv.CV_GRAY2RGB)
    
    #convert numpy mat to pixmap image
    qimg = QtGui.QImage(cvRGBImg.data,cvRGBImg.shape[1], cvRGBImg.shape[0], QtGui.QImage.Format_RGB888)
    
    #return qimg

    qpm = QtGui.QPixmap.fromImage(qimg)    

    return qpm




class ImageWidget(QWidget):
    """ A class for rendering video coming from OpenCV """
        
    def __init__(self):
        super(ImageWidget, self).__init__()
       
        data_path = '/homes/jannik/BVSiAB/RoadSegmentation_Tutorial'
        #data_path = '/home/jan/Downloads/RoadSegmentation_Tutorial/'
        load_dir_images = 'images/'
        load_dir_groundTruth = 'ground_truth/'
        data_dir = 'data/'
        stump_images = '_im_cr.ppm'
        #stump_images = 'jan.ppm'
        stump_groundTruth = '_la_cr.pgm'
        
        #objekts
        self.bev = BevTransformation()
        self.linefitter = LineFitting()
        self.edgedetection = EdgeDetection()
        self.polygonfitter = PolygonFitting()
        
        
        #get list of files in directory
        image_Data_loc = os.path.join(data_path,load_dir_images, '*'+stump_images)
        gt_Data_loc = os.path.join(data_path,load_dir_groundTruth, '*'+stump_groundTruth)
        self.image_Data_files = glob.glob(image_Data_loc)
        self.image_Data_files.sort()
        self.gt_Data_files = glob.glob(gt_Data_loc)
        self.gt_Data_files.sort()
        self.pos = 0

        cvBGRImg = cv2.imread(self.image_Data_files[self.pos])
        height, width, depth = cvBGRImg.shape
        self.qpm = convertIpl(cvBGRImg)
        self.qpm2 = convertIpl(cvBGRImg)
        self.qpm3 = convertIpl(cvBGRImg)
        self.qpm4 = convertIpl(cvBGRImg)
        self.setMinimumSize(width*2, height*3)
        self.setMaximumSize(self.minimumSize())
 
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Image')

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setPixmap(QtGui.QPixmap(self.qpm))
        self.imageLabel.setScaledContents(True)
        
        self.imageLabel2 = QtGui.QLabel()
        self.imageLabel2.setPixmap(QtGui.QPixmap(self.qpm2))
        self.imageLabel2.setScaledContents(True)
        
        self.imageLabel3 = QtGui.QLabel()
        self.imageLabel3.setPixmap(QtGui.QPixmap(self.qpm3))
        self.imageLabel3.setScaledContents(True)
        
        self.imageLabel4 = QtGui.QLabel()
        self.imageLabel4.setPixmap(QtGui.QPixmap(self.qpm4))
        self.imageLabel4.setScaledContents(True)
        #self.imageLabel.pixmap().scaled(QtCore.QSize(self.imageLabel.size()), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation) 
        #self.imageLabel.move(15, 10)

        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.imageLabel)
        hbox.addWidget(self.imageLabel2)
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.imageLabel3)
        hbox2.addWidget(self.imageLabel4)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.sdlText = QtGui.QLabel()
        self.sdlText.setText('set Min Threshold')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(30, 40, 100, 30)
        slda.valueChanged[int].connect(self.setMinTreshold)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText)
        sld.addWidget(slda)
        vbox.addLayout(sld)
        
        
        self.sdlText2 = QtGui.QLabel()
        self.sdlText2.setText('Set Max Treshold:')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(30, 40, 100, 30)
        slda.valueChanged[int].connect(self.setMaxTreshold)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText2)
        sld.addWidget(slda)
        vbox.addLayout(sld)
        
        
        
        self.sdlText3 = QtGui.QLabel()
        self.sdlText3.setText('Set X: ')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(0, 0, 300, 30)
        slda.valueChanged[int].connect(self.setX)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText3)
        sld.addWidget(slda)
        vbox.addLayout(sld)
        
        
        self.sdlText4 = QtGui.QLabel()
        self.sdlText4.setText('set Sobel:')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(30, 40, 100, 30)
        slda.valueChanged[int].connect(self.setSobel)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText4)
        sld.addWidget(slda)
        vbox.addLayout(sld)
        
        self.sdlText5 = QtGui.QLabel()
        self.sdlText5.setText('set Line Threshold:')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(30, 40, 100, 30)
        slda.valueChanged[int].connect(self.setLineThreshold)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText5)
        sld.addWidget(slda)
        
        vbox.addLayout(sld)
        
        self.sdlText6 = QtGui.QLabel()
        self.sdlText6.setText('set Line Length:')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(30, 40, 100, 30)
        slda.valueChanged[int].connect(self.setLineLength)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText6)
        sld.addWidget(slda)
        
        vbox.addLayout(sld)
        
        self.sdlText7 = QtGui.QLabel()
        self.sdlText7.setText('set K Size:')
        slda = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slda.setFocusPolicy(QtCore.Qt.NoFocus)
        slda.setGeometry(30, 40, 100, 30)
        slda.valueChanged[int].connect(self.setSobelKSize)
        sld = QtGui.QHBoxLayout()
        
        sld.addWidget(self.sdlText7)
        sld.addWidget(slda)
        
        vbox.addLayout(sld)
    
    
        vbox.addWidget(okButton)
        self.setLayout(vbox)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.queryFrame)
        self.timer.start(250)

    #def paintEvent(self, event):
     #   painter = QPainter(self)
        #painter.drawImage(QPoint(0, 0), self.qpm)

    def setMinTreshold(self, value):
        print 'slider changed to {0}'.format(value)
        self.edgedetection.setMinTresh(value)
        self.sdlText.setText('EDGE set Min Threshold:{0}'.format(value))
        
    def setMaxTreshold(self, value):
        print 'slider changed to {0}'.format(value)
        self.edgedetection.setMaxTresh(value)
        self.sdlText2.setText('EDGE set Max Threshold:{0}'.format(value))
    def setX(self, value):
        print 'slider changed to {0}'.format(value)
        self.bev.setAmount(value*4)
        self.sdlText3.setText('BEV set X Threshold:{0}'.format(value*4))
    def setSobel(self, value):
        print 'slider changed to {0}'.format(value)
        self.edgedetection.setSobel(value/10)
        self.sdlText4.setText('EDGE set Sobel:{0}'.format(value/10))
    def setSobelKSize(self, value):
        print 'slider changed to {0}'.format(value)
        self.edgedetection.setSobelKSize(value)   
        self.sdlText7.setText('EDGE set Sobel K/Canny AP Size:{0}'.format(value))
    def setLineThreshold(self, value):
        print 'slider changed to {0}'.format(value)
        self.linefitter.setThreshold(value)
        self.sdlText5.setText('LINE set Threshold:{0}'.format(value))        
    def setLineLength(self, value):
        print 'slider changed to {0}'.format(value)
        tmp = self.linefitter.setMinLength(value)
        self.sdlText6.setText('LINE set MinLength:{0}'.format(tmp))    
    
    def queryFrame(self):
        
#        cvBGRImg = cv2.imread(self.image_Data_files[self.pos])
        cvBGRImg = processImage(self.image_Data_files[self.pos])
        cvBGRImg2 = self.edgedetection.computeEdges(cvBGRImg)
        cvBGRImg2a = cv2.cvtColor(cvBGRImg2, cv2.cv.CV_GRAY2BGR)
        cvBGRImg3 = self.bev.computeBev(cvBGRImg2a)
        cvBGRImg3a = cv2.cvtColor(cvBGRImg3, cv2.cv.CV_BGR2GRAY)
        rev, cvBGRImg3a = cv2.threshold(cvBGRImg3a, 200 , 255, cv2.THRESH_BINARY)
        #cvBGRImg4 = self.linefitter.findLine(cvBGRImg3a)
        cvBGRImg5 = self.polygonfitter.findPolygon(cvBGRImg3a, cvBGRImg2.copy())
        self.bev.computePers(cvBGRImg5)

        #self.qpm4 = convertIplG(cvBGRImg4)
        self.qpm3 = convertIplG(cvBGRImg3a)
        self.qpm2 = convertIplG(cvBGRImg2)
        self.qpm = convertIpl(cvBGRImg)
        
        if(len(self.image_Data_files)>self.pos+1):
            self.pos += 1
        else:
            self.pos = 0
        
        self.imageLabel.setPixmap(self.qpm)
        self.imageLabel2.setPixmap(self.qpm2)
        self.imageLabel3.setPixmap(self.qpm3)
        self.imageLabel4.setPixmap(self.qpm4)


        #self.update()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    widget = ImageWidget()
    widget.show()
     
    sys.exit(app.exec_())

