from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import*
from PyQt6.uic import loadUi
import sys
import pandas as pd
import csv as md
import os


class Login_in(QMainWindow):
    def __init__(self):
        super(Login_in,self).__init__()
        uic.loadUi('dangnhap.ui',self)
        self.okdn.clicked.connect(self.login)
        self.OKDK.clicked.connect(self.reg_from)
    def reg_from(self):
            widget.setCurrentIndex(1)
    def login(self):
        name_input = self.user.text().strip()  # Lấy tên từ giao diện và loại bỏ khoảng trắng thừa
        pass_input = self.mk.text().strip()    # Lấy mật khẩu từ giao diện và loại bỏ khoảng trắng thừa
        print(name_input)
        # Đọc dữ liệu từ file CSV
        list1 = pd.read_csv('user.csv')

        # Kiểm tra xem người dùng và mật khẩu có khớp không
        if ((list1['Name'] == name_input) & (list1['Pass'] == pass_input)).any():
            QMessageBox.information(self, "Login output", "Đăng nhập thành công")
            widget.setCurrentIndex(3)
        else:
            QMessageBox.information(self, "Login output", "Đăng nhập thất bại")
class Login_up(QMainWindow):
    def __init__(self):
        super(Login_up,self).__init__()
        uic.loadUi('dangky.ui',self)
        self.okdk.clicked.connect(self.login)
        self.ql.clicked.connect(self.seg)
    def seg(self):
            widget.setCurrentIndex(0)
    def login(self):
        name = self.user.text()
        Pass = self.mk.text()
        print(name,Pass)
        list1 = md.connect('user.csv')
        query = list1.cursor()
        query.execute("select * from user_list where user= '"+name+"' and pass='"+Pass+"'")
        kt = query.fetchone()
        if kt:
            QMessageBox.information(self,"Loign output","Tai khoan ton tai")
            widget.setCurrentIndex(3)
        else:
            query.execute("insert into user_list values ('"+name+"','"+Pass+"')")
            list1.conmit()
            QMessageBox.information(self,"Loign output","Loign fail")
            widget.setCurrentIndex(1)
        
class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        uic.loadUi('lich.ui',self)
        self.ql.clicked.connect(self.seg)
    def seg(self):
         widget.setCurrentIndex(0)
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login_in = Login_in()
login_up = Login_up()
main = Main()
widget.addWidget(login_in)
widget.addWidget(login_up)
widget.addWidget(main)
widget.setCurrentIndex(0)
widget.setFixedHeight(450)
widget.setFixedWidth(750)
widget.show()
app.exec()
