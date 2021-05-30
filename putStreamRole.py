import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt
import subprocess
import os
import time




class Example(QMainWindow):

    

    def __init__(self,id):
        super().__init__()
        self.id=id
        self.initUI()

    def initUI(self):

        btnPushStream=QPushButton("开始推流",self)
        btnPushStream.move(50,50)

        btnCameraPushStream=QPushButton("结束推流",self)
        btnCameraPushStream.move(250,50)

        btnPushStream.clicked.connect(self.startPushStream)
        btnCameraPushStream.clicked.connect(self.endPushStream)

        self.setGeometry(300,300,400,400)
        self.setWindowTitle("推流客户端")

    ###有毛病这段代码
    # def ffmpeg(self):
    #     firstPartFfmpeg = 'ffmpeg -thread_queue_size 256 -f gdigrab -i desktop -f dshow -i audio="麦克风 (Realtek High Definition Audio)" -f dshow -i video="USB2.0 HD UVC WebCam" -filter_complex "[2]scale=iw/3:ih/3[pip];[0][pip]overlay=0:main_h-overlay_h" -vcodec libx264 -b:v 800k -r:v 25 -preset ultrafast -acodec aac -f flv rtmp://192.168.20.128:1935/'
    #     secondPartFfmpeg = self.id
    #     thirdPartFfmpeg = '/test'
    #     ffmpeger = subprocess.Popen(firstPartFfmpeg+str(secondPartFfmpeg)+thirdPartFfmpeg, shell=True, stdin=subprocess.PIPE)
    #     out = ffmpeger.communicate()[0]

    # proc = multiprocessing.Process(target=ffmpeg)
    
    def setStreamRoomId(self,rid):
        self.id=rid
    
    def startPushStream(self):
        # self.proc.start()
        firstPartFfmpeg ='ffmpeg -thread_queue_size 256 -f gdigrab -i desktop -f dshow -i audio="麦克风 (Realtek High Definition Audio)" -f dshow -i video="USB2.0 HD UVC WebCam" -filter_complex "[2]scale=iw/3:ih/3[pip];[0][pip]overlay=0:main_h-overlay_h" -vcodec libx264 -b:v 800k -r:v 25 -preset ultrafast -acodec aac -f flv rtmp://192.168.20.128:1935/hls1/'
        secondPartFfmpeg=self.id
        p = subprocess.Popen(firstPartFfmpeg+str(secondPartFfmpeg), shell=True, stdin=subprocess.PIPE)




    def endPushStream(self):
        kill_command = 'taskkill /f /im ffmpeg.exe'
        cc = subprocess.Popen(kill_command, shell=True)
        # self.proc.terminate()

            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
