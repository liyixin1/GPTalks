import bcrypt
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog, QMessageBox

import pydb
from ui.changepwd_diglog_ui import Ui_changepwd_Dialog


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class ChangePwdDialog(QDialog, Ui_changepwd_Dialog):
    change_complete = pyqtSignal()

    def __init__(self):
        super(ChangePwdDialog, self).__init__()
        self.setupUi(self)

    def check_password(self, hashed_password, user_password):
        # 确保 hashed_password 是 bytes 类型
        hashed_password = bytes(hashed_password)

        # 将用户输入的密码转化为二进制字符串
        user_password = user_password.encode('utf-8')

        # 检查用户输入的密码经过哈希后是否与我们存储的哈希值相匹配
        return bcrypt.checkpw(user_password, hashed_password)

    def accept(self):
        userpwd = pydb.select_one_date("password_hash", "users", "username", self.lineEdit_name.text())

        if self.lineEdit_name.text() == "" or self.lineEdit_currentpwd == "" \
                or self.lineEdit_newpwd.text() == "" or self.lineEdit_newpwd2.text() == "":
            QMessageBox.warning(self, "错误", "不能有空！")
        elif pydb.select_one_date("username", "users", "username", self.lineEdit_name.text()) \
                is None or self.check_password(userpwd, self.lineEdit_currentpwd.text()) is not True:
            print(self.check_password(userpwd, self.lineEdit_currentpwd.text()))
            QMessageBox.warning(self, "错误", "用户名或密码错误！")
        elif self.lineEdit_newpwd.text() == self.lineEdit_currentpwd.text():
            QMessageBox.warning(self, "错误", "新密码不能与原密码相同。")
        elif self.lineEdit_newpwd.text() != self.lineEdit_newpwd2.text():
            QMessageBox.warning(self, "错误", "密码不一致！")
        else:
            newpwd = hash_password(self.lineEdit_newpwd.text())
            pydb.up_one_date("users", "password_hash", newpwd, "username", self.lineEdit_name.text())
            QMessageBox.information(self, "成功", "修改成功。")
            self.change_complete.emit()
