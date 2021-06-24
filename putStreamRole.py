import sys
from PyQt5.QtWidgets import QComboBox, QLabel, QMainWindow, QPushButton, QWidget, QApplication
from PyQt5.QtCore import QSize, Qt
import subprocess
import os
import time




class Example(QMainWindow):

    

    def __init__(self,id):
        super().__init__()
        self.id=id
        self.initUI()

    def initUI(self):


        label1=QLabel(self)
        label1.setText("请选择摄像头")
        label1.resize(QSize(200,30))
        label1.move(50,70)

        label2 = QLabel(self)
        label2.setText("请选择麦克风")
        label2.resize(QSize(200, 30))
        label2.move(500, 70)

        cbForCamera=QComboBox(self)
        cbForCamera.resize(QSize(220,30))
        cbForCamera.move(50,150)
        cameraList=self.listAllTheCameraDevices()
        for camera in cameraList:
            cbForCamera.addItem(camera)
        
        cbForAudio = QComboBox(self)
        cbForAudio.resize(QSize(250,30))
        cbForAudio.move(500, 150)
        audioList = self.listAllTheAudioDevices()
        for audio in audioList:
            cbForAudio.addItem(audio)
        
        # camera=cbForCamera.currentText()
        # audio=cbForAudio.currentText()
        # print(camera)
        # print(audio)

    
        btnPushStream=QPushButton("开始推流",self)
        btnPushStream.move(50,450)


        btnPaintTool = QPushButton("开启白板", self)
        btnPaintTool.move(350, 275)

        btnCameraPushStream=QPushButton("结束推流",self)
        btnCameraPushStream.move(500,450)

        btnPushStream.clicked.connect(
            lambda:self.startPushStream(cbForCamera.currentText(), cbForAudio.currentText()))
        btnCameraPushStream.clicked.connect(self.endPushStream)
        btnPaintTool.clicked.connect(self.startPaintTool)

        self.setGeometry(400,400,800,700)
        self.setWindowTitle("推流客户端")

    
    
    def setStreamRoomId(self,rid):
        self.id=rid
    

    def startPushStream(self,camera,audio):
        firstPartFfmpeg ='ffmpeg -thread_queue_size 256 -f gdigrab -i desktop -f dshow -i audio="'
        secondPartFfmpeg = '" -f dshow -i video="'
        thirdPartFfmpeg = '" -filter_complex "[2]scale=iw/3:ih/3[pip];[0][pip]overlay=0:main_h-overlay_h" -vcodec libx264 -b:v 800k -r:v 25 -preset ultrafast -acodec aac -f flv rtmp://10.40.23.175:1935/hls1/'
        fourthPartFfmpeg=self.id
        # print(firstPartFfmpeg+audio+secondPartFfmpeg +camera+thirdPartFfmpeg+str(fourthPartFfmpeg))
        p = subprocess.Popen(firstPartFfmpeg+audio+secondPartFfmpeg+camera+thirdPartFfmpeg+str(fourthPartFfmpeg), shell=True, stdin=subprocess.PIPE)


    def startPaintTool(self):
         p= subprocess.Popen("python paintTool.py", shell=True)

    def endPushStream(self):
        kill_command = 'taskkill /f /im ffmpeg.exe'
        cc = subprocess.Popen(kill_command, shell=True)
        # self.proc.terminate()

    def listAllTheCameraDevices(self):
        cmd = ['ffmpeg', '-list_devices', 'true', '-f', 'dshow', '-i', 'dummy']
        device_list = []
        process = subprocess.Popen(
            cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        record = False
        num_line = 0
        for line in process.stdout:
            if record:
                if line.startswith("[dshow"):
                    _line = line[index + 2:]
                    if _line.startswith("DirectShow audio"):
                        break
                    if _line.startswith("DirectShow video"):
                        record = False
                    if record and num_line % 2 == 0:
                        device_list.append(_line[2:len(_line)-2])
                    num_line += 1

            if line.startswith("[dshow"):
                index = line.find("]")
                if index > 0:
                    _line = line[index+2:]
                    if _line.startswith("DirectShow video"):
                        # print('>>>>>>>', _line)
                        num_line = 0
                        record = True
        return device_list

    def listAllTheAudioDevices(self):
        cmd = ['ffmpeg', '-list_devices', 'true', '-f', 'dshow', '-i', 'dummy']
        device_list = []
        process = subprocess.Popen(
            cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        record = False
        num_line = 0
        for line in process.stdout:
            if record:
                if line.startswith("[dshow"):
                    _line = line[index + 2:]
                    if _line.startswith("DirectShow audio"):
                        record = False
                    if record and num_line % 2 == 0:
                        device_list.append(_line[2:len(_line)-2])
                    num_line += 1

            if line.startswith("[dshow"):
                index = line.find("]")
                if index > 0:
                    _line = line[index+2:]
                    if _line.startswith("DirectShow audio"):
                        # print('>>>>>>>', _line)
                        num_line = 0
                        record = True
        return device_list
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
