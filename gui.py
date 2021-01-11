from PIL import Image
import sys
import os.path
from PyQt5.QtWidgets import *

# GUI codes from https://wikidocs.net/5247

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 100)
        self.setWindowTitle("Image Toukorization")

        self.pushButton = QPushButton("Open your image!")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0] != '':
            self.processing(fname[0])
    
    def processing(self, path):
        dirname = os.path.dirname(path)
        filename = os.path.splitext(os.path.basename(path))[0]

        # image processing function
        # Open the image
        image = Image.open(path)
        # Create a new image
        after = Image.new("RGBA", image.size, (255, 255, 255, 255))

        # Create a mask to add transparency
        mask = image.convert('L')
        # Put transparent mask
        after.putalpha(mask)
        # Save the created image
        after.save(dirname + "/mod_" + filename + ".png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
