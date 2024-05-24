import bcrypt
from PyQt6.QtCore import pyqtSignal, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QDialog, QMessageBox
from ui.signup_dialog_ui import Ui_signup_dialog
import pydb


# 密码处理函数
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class SignupDialog(QDialog, Ui_signup_dialog):
    registration_complete = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(self.on_submit_button_clicked)

        # 使用 Python 的 re 模块来构建正则表达式
        pattern = r'^[\w-]{6,10}$'
        regex = QRegularExpression(pattern)
        validator = QRegularExpressionValidator(regex, self)
        self.lineEdit_username.setValidator(validator)

    def on_submit_button_clicked(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if not username or not password:
            QMessageBox.warning(self, "错误", "用户名和密码不能为空！")
            return
        elif pydb.select_one_date("username", "users", "username", username) is not None:
            QMessageBox.warning(self, "错误", "用户名已存在！")
            return
        hashed = hash_password(password)
        pydb.insert_date(username, hashed)
        pydb.insert_one_date(username)
        QMessageBox.information(self, "成功", "注册成功！")
        self.registration_complete.emit()
