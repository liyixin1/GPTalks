import bcrypt
from PyQt6.QtCore import pyqtSignal, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QDialog, QMessageBox

import pydb
from ui.login_dialog_ui import Ui_Login_Dialog


class LoginDialog(QDialog, Ui_Login_Dialog):
    goto_registration = pyqtSignal()
    login_successful = pyqtSignal()
    goto_changepwd = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_name = None
        self.pushButton_login.clicked.connect(self.on_login_button_clicked)
        self.pushButton_signup.clicked.connect(self.on_signup_button_clicked)
        self.pushButton_changepwd.clicked.connect(self.on_changepwd_button_clicked)

        pattern = r'^[\w-]{6,10}$'
        regex = QRegularExpression(pattern)
        validator = QRegularExpressionValidator(regex, self)
        self.lineEdit_username.setValidator(validator)

    def check_password(self, hashed_password, user_password):
        # 确保 hashed_password 是 bytes 类型
        hashed_password = bytes(hashed_password)

        # 将用户输入的密码转化为二进制字符串
        user_password = user_password.encode('utf-8')

        # 检查用户输入的密码经过哈希后是否与我们存储的哈希值相匹配
        return bcrypt.checkpw(user_password, hashed_password)

    def on_login_button_clicked(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if username == "" or password == "":
            QMessageBox.warning(self, "错误", "用户名或密码不能为空！")
            return
        elif pydb.select_one_date("username", "users", "username", username) is None:
            QMessageBox.warning(self, "错误", "用户名不存在！")
            return
        pwd = pydb.select_one_date("password_hash", "users", "username", username)
        if pwd and self.check_password(pwd, password):
            self.user_name = username
            self.login_successful.emit()
        else:
            QMessageBox.warning(self, "失败", "用户名或密码错误！")

    def on_signup_button_clicked(self):
        self.goto_registration.emit()

    def on_changepwd_button_clicked(self):
        self.goto_changepwd.emit()