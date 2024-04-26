# Form implementation generated from reading ui file 'C:\Users\13677\Desktop\graduation_project\GPTalks\ui\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/windows_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.splitter_2)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtWidgets.QLabel(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)
        self.label_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.label_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.label_icon.setText("")
        self.label_icon.setScaledContents(True)
        self.label_icon.setWordWrap(False)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_name = QtWidgets.QLabel(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMaximumSize(QtCore.QSize(100, 40))
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_logout = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_logout.sizePolicy().hasHeightForWidth())
        self.pushButton_logout.setSizePolicy(sizePolicy)
        self.pushButton_logout.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_logout.setCheckable(True)
        self.pushButton_logout.setAutoRepeat(False)
        self.pushButton_logout.setAutoExclusive(False)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.listWidget_session = QtWidgets.QListWidget(parent=self.layoutWidget_3)
        self.listWidget_session.setObjectName("listWidget_session")
        self.verticalLayout_4.addWidget(self.listWidget_session)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_new = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/new.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_new.setIcon(icon1)
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout_3.addWidget(self.pushButton_new)
        self.pushButton_delect = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/delect.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_delect.setIcon(icon2)
        self.pushButton_delect.setObjectName("pushButton_delect")
        self.horizontalLayout_3.addWidget(self.pushButton_delect)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.pushButton_settings = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/setting.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_settings.setIcon(icon3)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.verticalLayout_4.addWidget(self.pushButton_settings)
        self.pushButton_about = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/about.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_about.setIcon(icon4)
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_4.addWidget(self.pushButton_about)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_5.addWidget(self.lineEdit_name)
        self.splitter_3 = QtWidgets.QSplitter(parent=self.verticalLayoutWidget_2)
        self.splitter_3.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.textBrowser_show = QtWidgets.QTextBrowser(parent=self.splitter_3)
        self.textBrowser_show.setObjectName("textBrowser_show")
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.splitter_3)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.plainTextEdit_input = QtWidgets.QPlainTextEdit(parent=self.layoutWidget_4)
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")
        self.horizontalLayout_4.addWidget(self.plainTextEdit_input)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_audio = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        self.pushButton_audio.setCheckable(True)
        self.pushButton_audio.setChecked(False)
        self.pushButton_audio.setAutoRepeat(False)
        self.pushButton_audio.setObjectName("pushButton_audio")
        self.verticalLayout_2.addWidget(self.pushButton_audio)
        self.pushButton_commit = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/commit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_commit.setIcon(icon5)
        self.pushButton_commit.setObjectName("pushButton_commit")
        self.verticalLayout_2.addWidget(self.pushButton_commit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.splitter_3)
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GPTalks"))
        self.label_name.setText(_translate("MainWindow", "用户1"))
        self.pushButton_logout.setText(_translate("MainWindow", "登录"))
        self.pushButton_new.setText(_translate("MainWindow", " 新建会话"))
        self.pushButton_delect.setText(_translate("MainWindow", " 删除会话"))
        self.pushButton_settings.setText(_translate("MainWindow", " 设置"))
        self.pushButton_about.setText(_translate("MainWindow", " 关于"))
        self.plainTextEdit_input.setPlaceholderText(_translate("MainWindow", "发送消息给 GPTalks..."))
        self.pushButton_audio.setText(_translate("MainWindow", "语音"))
        self.pushButton_commit.setText(_translate("MainWindow", " 提交"))
