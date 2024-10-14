from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import pandas as pd
import os


class Login_in(QMainWindow):
    def __init__(self):
        super(Login_in, self).__init__()
        uic.loadUi('dangnhap.ui', self)
        self.okdn.clicked.connect(self.login)
        self.OKDK.clicked.connect(self.reg_from)

    def reg_from(self):
        widget.setCurrentIndex(1)

    def login(self):
        name_input = self.user.text().strip()  # Lấy tên từ giao diện và loại bỏ khoảng trắng thừa
        pass_input = self.mk.text().strip()    # Lấy mật khẩu từ giao diện và loại bỏ khoảng trắng thừa)
        # Đọc dữ liệu từ file CSV
        list1 = pd.read_csv('user1.csv')
        user_exists = list1['Name'].str.contains(name_input, case=False, na=False)
       
        if user_exists.any():  # Check if any user matches
            # Get the user's password (if multiple matches, this will take the first)
            user_password = list1.loc[user_exists, 'Pass'].values[0]  
            
            # Check password (ensure both are strings)
            if str(user_password) == str(pass_input):
                QMessageBox.warning(self, "Đăng nhập", "Đăng nhập thành công")
                widget.setCurrentIndex(2)
            else:
                QMessageBox.warning(self, "Đăng nhập", "Sai mậ khẩu")
        else:
            QMessageBox.warning(self, "Đăng nhập", "Sai tài khoản")


class Login_up(QMainWindow):
    def __init__(self):
        super(Login_up, self).__init__()
        uic.loadUi('dangky.ui', self)
        self.okdk.clicked.connect(self.register)
        self.ql.clicked.connect(self.seg)

    def seg(self):
        widget.setCurrentIndex(2)

    def register(self):
        name_input = self.user.text().strip()
        pass_input = self.mk.text().strip()
        email_input = self.email.text().strip()
        user_input = self.name.text().strip()
        # Kiểm tra dữ liệu người dùng nhập
        if not name_input and not pass_input and not email_input and not user_input:
            QMessageBox.warning(self, "Đăng ký", "Không được để trống")
            return

        # Đọc file CSV (nếu file đã tồn tại)
        if os.path.exists('user1.csv'):
            df = pd.read_csv('user1.csv')

            # Kiểm tra xem người dùng đã tồn tại chưa
            if (df['Name'] == name_input).any():
                QMessageBox.warning(self, "Đăng ký", "Tài khoản đã tồn tại")
            else:
                # Thêm người dùng mới vào file CSV
                new_user = pd.DataFrame({'Name': [name_input], 'Pass': [pass_input], 'email': [email_input], 'user': [user_input]})
                new_user.to_csv('user1.csv', mode='a', header=False, index=False)
                QMessageBox.information(self, "Đăng ký", "Đăng ký thành công")
                widget.setCurrentIndex(2)
        else:
            # Tạo file mới nếu file chưa tồn tại và thêm người dùng
            new_user = pd.DataFrame({'Name': [name_input], 'Pass': [pass_input], 'email': [email_input], 'user': [user_input]})
            new_user.to_csv('user1.csv', mode='w', header=True, index=False)
            QMessageBox.information(self, "Đăng ký", "Đăng ký thành công")
            widget.setCurrentIndex(2)


class Main1(QMainWindow):
    def __init__(self):
        super(Main1, self).__init__()
        uic.loadUi('lich.ui', self)
        self.ql.clicked.connect(self.seg)
        self.lich.clicked.connect(self.main2)
    def seg(self):
        widget.setCurrentIndex(0)

    def main2(self):
        widget.setCurrentIndex(3)
    
class Main2(QMainWindow):
    def  __init__(self):
        super(Main2, self).__init__()
        uic.loadUi('lichs.ui', self)
        self.ql.clicked.connect(self.seg)
        self.thongbao.clicked.connect(self.main1)

    def seg(self):
        widget.setCurrentIndex(0)
        
    def main1(self):
        widget.setCurrentIndex(2)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login_in = Login_in()
login_up = Login_up()
main1 = Main1()
main2 = Main2()
widget.addWidget(login_in)
widget.addWidget(login_up)
widget.addWidget(main1)
widget.addWidget(main2)
widget.setCurrentIndex(0)
widget.setFixedHeight(450)
widget.setFixedWidth(750)
widget.show()
app.exec()
