import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel, QLineEdit)
from PyQt5.QtGui import QPixmap
import app
import torch
from diffusers import StableDiffusionPipeline


class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")
        self.label = QLabel(self)
        
         
        # loading image
        self.pixmap = QPixmap('image.png')
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
        
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.label.move(10,10)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.title = "AI Image Generator"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowTitle("AI Redefined")
        self.label = QLabel(self)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        self.pushButton = QPushButton("generate Image", self)
        self.pushButton.move(320, 25)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")
        

        self.pushButton.clicked.connect(self.fun) 
        
        self.b1 = QPushButton("View Image", self)
        self.b1.move(450, 25)
        self.b1.setToolTip("<h3>Start the Session</h3>")
        self.b1.setEnabled(False)

        self.b1.clicked.connect(self.window2)
        
        
        



        self.main_window()

    def fun(self):
        textboxValue = self.textbox.text()
        self.model(textboxValue)
        self.b1.setEnabled(True)




    def main_window(self):
        self.label = QLabel("AI Redined", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                             # <===
        self.w = Window2()
       
        self.w.show()
    def model(self,a):
        if torch.cuda.is_available():
            model_id = "CompVis/stable-diffusion-v1-4"
            device = "cuda"


            pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
            pipe = pipe.to(device)

            prompt = a
            image = pipe(prompt, guidance_scale=8.5).images[0]  
    
            image.save("image.png")

        else:
            torch.cuda.empty_cache()
            self.hello(a)
        return 1
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())