# Form implementation generated from reading ui file 'C:\Users\13677\Desktop\graduation_project\GPTalks\ui\signup_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_signup_dialog(object):
    def setupUi(self, signup_dialog):
        signup_dialog.setObjectName("signup_dialog")
        signup_dialog.setEnabled(True)
        signup_dialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(signup_dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(parent=signup_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_1.setStyleSheet("font: 20pt \"Microsoft YaHei UI\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_1.setFrame(False)
        self.lineEdit_1.setDragEnabled(False)
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=signup_dialog)
        self.lineEdit_2.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=signup_dialog)
        self.lineEdit_username.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.lineEdit_username.setClearButtonEnabled(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=signup_dialog)
        self.lineEdit_password.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.pushButton_submit = QtWidgets.QPushButton(parent=signup_dialog)
        self.pushButton_submit.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgba(0, 133, 255,255);")
        self.pushButton_submit.setDefault(False)
        self.pushButton_submit.setFlat(False)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.verticalLayout.addWidget(self.pushButton_submit)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(signup_dialog)
        QtCore.QMetaObject.connectSlotsByName(signup_dialog)

    def retranslateUi(self, signup_dialog):
        _translate = QtCore.QCoreApplication.translate
        signup_dialog.setWindowTitle(_translate("signup_dialog", "注册"))
        self.lineEdit_1.setText(_translate("signup_dialog", "欢迎注册GPTalks"))
        self.lineEdit_2.setText(_translate("signup_dialog", "每一天，乐在沟通。"))
        self.lineEdit_username.setPlaceholderText(_translate("signup_dialog", "用户名"))
        self.lineEdit_password.setPlaceholderText(_translate("signup_dialog", "密码"))
        self.pushButton_submit.setWhatsThis(_translate("signup_dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_submit.setText(_translate("signup_dialog", "立即注册"))
