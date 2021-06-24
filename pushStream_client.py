from putStreamRole import Example
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from loginUIpage import *
from putStreamRole import *
import pymysql

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        db = pymysql.connect(host='localhost', user='root',
                             passwd='123456', db='streamdb', charset='utf8')
        cursor = db.cursor()
        sql = "select count(*) from user where name='%s' and password='%s' " % (username,password)
        cursor.execute(sql)
        data = cursor.fetchone()
        resultNum = data[0]
        if resultNum==1:
            # print("login success")
            sql2 = "select id from streamroom where anchorname='%s'" % (username)
            cursor.execute(sql2)
            data2 = cursor.fetchone()
            rid = data2[0]
            db.close()
            ex.show()
            ex.setStreamRoomId(rid)
            self.close()
        else:
            # print("login failed")
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '密码输入错误或用户名不存在，登录失败！')
            msg_box.exec_()


if __name__=='__main__':

    app=QApplication(sys.argv)
    myWin=MyWindow()
    ex = Example('1')
    myWin.show()
    sys.exit(app.exec_())
