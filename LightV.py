import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QAction,
    QFileDialog, QDesktopWidget, QMessageBox, QSizePolicy, QToolBar, QStatusBar,
    QDockWidget, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PIL import Image
from lightVSoftware import Ui_LightV

#class LightV(QtWidgets.QWidget):
class LightV(QtWidgets.QMainWindow):

    def __init__(self):
        super(LightV, self).__init__()
        self.ui = Ui_LightV()
        self.ui.setupUi(self)

        self.initializeUI()

        self.show()

    def initializeUI(self):
        self.image = QPixmap()
        self.image_label = self.ui.canvas

        self.ui.actionOpen.triggered.connect(self.openImage)
        #self.ui.actionPrint.triggered.connect()
        self.ui.actionPrint.setEnabled(False) # Make print action inenabled on Start
        self.ui.actionClear.triggered.connect(self.clearCanvas)
        self.ui.actionSave_Image_As_.triggered.connect(self.saveImage)
        # Lambda for passing Arguments
        self.ui.actionRotate_Left.triggered.connect(lambda: self.rotateImage90(90)) # Lambda for passing Args
        self.ui.pushButton_1.clicked.connect(lambda: self.rotateImage90(-90))
        self.ui.actionRotate_Right.triggered.connect(lambda: self.rotateImage90(-90))
        self.ui.pushButton_2.clicked.connect(lambda: self.rotateImage90(90))
        self.ui.pushButton_8.clicked.connect(self.grayScale)

    def rotateImage90(self, angle = -90):
        """
        Rotate image 90º clockwise
        """
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(angle)
            pixmap = QPixmap(self.image)

            rotated = pixmap.transformed(transform90, mode=Qt.SmoothTransformation)

            self.image_label.setPixmap(rotated.scaled(self.image_label.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint() # repaint the child widget
        else:
            # No image to rotate
            pass

    def grayScale(self):
        """
        GrayScale Solution
        """
        if self.image.isNull() == False:
            self.grayScaleImage()
            pixmap = QPixmap('temp.png')
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(pixmap)
            self.image_label.repaint() # repaint the child widget
        else:
            # No image to rotate
            pass

    def grayScaleImage(self):
        img = Image.open(self.current_image_file)
        width, height = img.size
        new = Image.new("RGB", (width, height), "white")

        pixels = new.load()
        for i in range(width):
            for j in range(height):
                # Get Pixel
                pixel = img.getpixel((i, j))
                # Get R, G, B values (This are int from 0 to 255)
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]
                # Transform to grayscale
                gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

                # Set Pixel in new image
                pixels[i, j] = (int(gray), int(gray), int(gray))

        #new.show()
        new.save('temp.png')

    def clearCanvas(self):
        self.ui.canvas.clear() #self.ui.canvas
        #Set print to enabled now
        self.ui.actionPrint.setEnabled(False)

    def openImage(self):
        """
        Open an image file and display its contents in label widget.
        Display error message if image can't be opened.
        """
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image",
            "", "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;\
                GIF Files (*.gif)")


        if image_file:
            self.current_image_file = image_file
            self.image = QPixmap(image_file)
            self.image_label = self.ui.canvas
            #self.image_label.setText("Ben MULONGO")
            self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            #self.image_label.move(40,50)
            # Set print to enabled now
            self.ui.actionPrint.setEnabled(True)

        else:
            QMessageBox.information(self, "Error",
                "Unable to open image.", QMessageBox.Ok)

    def saveImage(self):
        """
        Save the image.
        Display error message if image can't be saved.
        """
        image_file, _ = QFileDialog.getSaveFileName(self, "Save Image",
            "", "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;\
                GIF Files (*.gif)")

        if image_file and self.image.isNull() == False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Error",
                "Unable to save image.", QMessageBox.Ok)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LightV()
    sys.exit(app.exec_())