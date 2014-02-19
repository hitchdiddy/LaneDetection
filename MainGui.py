import cv2
import numpy as np
import os
import sys
import glob
import math
from BevTransformation import BevTransformation

from LineFitting import LineFitting
from EdgeDetection import EdgeDetection
from PyQt4 import QtCore, QtGui 

from PyQt4.QtCore import QPoint, QTimer
from PyQt4.QtGui import QApplication, QImage, QWidget



def processImage(filename):

    print 'processing'
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
        stump_groundTruth = '_la_cr.pgm'
        
        #objekts
        self.bev = BevTransformation()
        self.linefitter = LineFitting()
        self.edgedetection = EdgeDetection()
        
        
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
        self.setMinimumSize(width, height)
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
        #self.imageLabel.pixmap().scaled(QtCore.QSize(self.imageLabel.size()), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation) 
        #self.imageLabel.move(15, 10)

        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        sld2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld2.setFocusPolicy(QtCore.Qt.NoFocus)
        sld2.setGeometry(30, 40, 100, 30)
        sld2.valueChanged[int].connect(self.changeValue)
        
        sld3 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld3.setFocusPolicy(QtCore.Qt.NoFocus)
        sld3.setGeometry(30, 40, 100, 30)
        sld3.valueChanged[int].connect(self.changeValue)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.imageLabel)
        hbox.addWidget(self.imageLabel2)
        hbox.addWidget(self.imageLabel3)
        hbox.addWidget(okButton)
        
        
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(sld)
        vbox.addWidget(sld2)
        vbox.addWidget(sld3)
        self.setLayout(vbox)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.queryFrame)
        self.timer.start(250)

    #def paintEvent(self, event):
     #   painter = QPainter(self)
        #painter.drawImage(QPoint(0, 0), self.qpm)

    def changeValue(self, value):
        print 'slider changed to {0}'.format(value)

    def queryFrame(self):
        
#        cvBGRImg = cv2.imread(self.image_Data_files[self.pos])
        cvBGRImg = processImage(self.image_Data_files[self.pos])
        self.qpm = convertIpl(cvBGRImg)
        cvBGRImg = self.bev.computeBev(cvBGRImg)
        self.qpm2 = convertIpl(cvBGRImg)
        cvBGRImg = self.linefitter.findLine(cvBGRImg)
        self.qpm3 = convertIpl(cvBGRImg)
        self.pos += 1
        self.qpm = convertIpl(cvBGRImg)
        self.imageLabel.setPixmap(self.qpm)
        #self.update()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    widget = ImageWidget()
    widget.show()
     
    sys.exit(app.exec_())

