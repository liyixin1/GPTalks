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
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setHandleWidth(2)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.splitter_2)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_session = QtWidgets.QListWidget(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_session.sizePolicy().hasHeightForWidth())
        self.listWidget_session.setSizePolicy(sizePolicy)
        self.listWidget_session.setIconSize(QtCore.QSize(20, 20))
        self.listWidget_session.setObjectName("listWidget_session")
        self.verticalLayout_4.addWidget(self.listWidget_session)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_new_chat = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_new_chat.setIcon(icon1)
        self.pushButton_new_chat.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_new_chat.setObjectName("pushButton_new_chat")
        self.horizontalLayout_3.addWidget(self.pushButton_new_chat)
        self.pushButton_new_images = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/new_image.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_new_images.setIcon(icon2)
        self.pushButton_new_images.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_new_images.setObjectName("pushButton_new_images")
        self.horizontalLayout_3.addWidget(self.pushButton_new_images)
        self.pushButton_delect = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_delect.setIcon(icon3)
        self.pushButton_delect.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_delect.setCheckable(False)
        self.pushButton_delect.setAutoDefault(False)
        self.pushButton_delect.setDefault(False)
        self.pushButton_delect.setFlat(False)
        self.pushButton_delect.setObjectName("pushButton_delect")
        self.horizontalLayout_3.addWidget(self.pushButton_delect)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.pushButton_settings = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_settings.setIcon(icon4)
        self.pushButton_settings.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.verticalLayout_4.addWidget(self.pushButton_settings)
        self.pushButton_about = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/about.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_about.setIcon(icon5)
        self.pushButton_about.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_4.addWidget(self.pushButton_about)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_name.setClearButtonEnabled(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_5.addWidget(self.lineEdit_name)
        self.splitter_3 = QtWidgets.QSplitter(parent=self.verticalLayoutWidget_2)
        self.splitter_3.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_3.setHandleWidth(2)
        self.splitter_3.setObjectName("splitter_3")
        self.textBrowser_show = QtWidgets.QTextBrowser(parent=self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.textBrowser_show.setFont(font)
        self.textBrowser_show.setStyleSheet("")
        self.textBrowser_show.setReadOnly(True)
        self.textBrowser_show.setOpenExternalLinks(True)
        self.textBrowser_show.setObjectName("textBrowser_show")
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.splitter_3)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_upload = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        self.pushButton_upload.setToolTipDuration(-1)
        self.pushButton_upload.setStatusTip("")
        self.pushButton_upload.setWhatsThis("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/upload.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_upload.setIcon(icon6)
        self.pushButton_upload.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_upload.setAutoDefault(False)
        self.pushButton_upload.setDefault(False)
        self.pushButton_upload.setFlat(False)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.horizontalLayout.addWidget(self.pushButton_upload, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_send = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        self.pushButton_send.setStatusTip("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:\\Users\\13677\\Desktop\\graduation_project\\GPTalks\\ui\\image/send.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_send.setIcon(icon7)
        self.pushButton_send.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_send.setFlat(False)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout.addWidget(self.pushButton_send, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.plainTextEdit_input = QtWidgets.QPlainTextEdit(parent=self.layoutWidget_4)
        self.plainTextEdit_input.setEnabled(True)
        self.plainTextEdit_input.setToolTip("")
        self.plainTextEdit_input.setUndoRedoEnabled(True)
        self.plainTextEdit_input.setOverwriteMode(False)
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")
        self.verticalLayout_6.addWidget(self.plainTextEdit_input)
        self.verticalLayout_5.addWidget(self.splitter_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_image = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_image.setMaximumSize(QtCore.QSize(80, 80))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.horizontalLayout_2.addWidget(self.label_image, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_file = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_file.setMinimumSize(QtCore.QSize(0, 0))
        self.label_file.setMaximumSize(QtCore.QSize(80, 80))
        self.label_file.setText("")
        self.label_file.setObjectName("label_file")
        self.horizontalLayout_2.addWidget(self.label_file, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
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
        self.pushButton_new_chat.setText(_translate("MainWindow", " 新建对话"))
        self.pushButton_new_images.setText(_translate("MainWindow", "新图片"))
        self.pushButton_delect.setText(_translate("MainWindow", " 删除对话"))
        self.pushButton_settings.setText(_translate("MainWindow", " 设置"))
        self.pushButton_about.setText(_translate("MainWindow", " 关于"))
        self.textBrowser_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI Emoji\';\"><br /></p></body></html>"))
        self.pushButton_upload.setToolTip(_translate("MainWindow", "支持上传1张图片\n"
"最大20MB"))
        self.pushButton_upload.setText(_translate("MainWindow", "图片"))
        self.pushButton_send.setToolTip(_translate("MainWindow", "[回车键]换行，[ctrl+回车键]发送"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))
        self.plainTextEdit_input.setPlaceholderText(_translate("MainWindow", "发送消息给 GPTalks..."))
