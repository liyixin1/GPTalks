# Form implementation generated from reading ui file 'C:\Users\13677\Desktop\graduation_project\GPTalks\ui\settings_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_settings_dialog(object):
    def setupUi(self, settings_dialog):
        settings_dialog.setObjectName("settings_dialog")
        settings_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        settings_dialog.resize(600, 400)
        settings_dialog.setMinimumSize(QtCore.QSize(600, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(settings_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=settings_dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_model = QtWidgets.QWidget()
        self.tab_model.setObjectName("tab_model")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_model)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_AI = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_AI.setStyleSheet("background-color: transparent;")
        self.lineEdit_AI.setFrame(False)
        self.lineEdit_AI.setReadOnly(True)
        self.lineEdit_AI.setObjectName("lineEdit_AI")
        self.verticalLayout_3.addWidget(self.lineEdit_AI)
        self.comboBox_AI = QtWidgets.QComboBox(parent=self.tab_model)
        self.comboBox_AI.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.comboBox_AI.setEditable(False)
        self.comboBox_AI.setObjectName("comboBox_AI")
        self.verticalLayout_3.addWidget(self.comboBox_AI)
        self.line = QtWidgets.QFrame(parent=self.tab_model)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(30)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_api_key_title = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_api_key_title.setStyleSheet("background-color: transparent;")
        self.lineEdit_api_key_title.setFrame(False)
        self.lineEdit_api_key_title.setReadOnly(True)
        self.lineEdit_api_key_title.setObjectName("lineEdit_api_key_title")
        self.verticalLayout_5.addWidget(self.lineEdit_api_key_title)
        self.lineEdit_key = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_key.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.lineEdit_key.setText("")
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.verticalLayout_5.addWidget(self.lineEdit_key)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_model_title = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_model_title.setStyleSheet("background-color: transparent;")
        self.lineEdit_model_title.setFrame(False)
        self.lineEdit_model_title.setReadOnly(True)
        self.lineEdit_model_title.setObjectName("lineEdit_model_title")
        self.verticalLayout_6.addWidget(self.lineEdit_model_title)
        self.comboBox_model = QtWidgets.QComboBox(parent=self.tab_model)
        self.comboBox_model.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.comboBox_model.setEditable(False)
        self.comboBox_model.setObjectName("comboBox_model")
        self.verticalLayout_6.addWidget(self.comboBox_model)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_maxtokens_title = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_maxtokens_title.setStyleSheet("background-color: transparent;")
        self.lineEdit_maxtokens_title.setFrame(False)
        self.lineEdit_maxtokens_title.setReadOnly(True)
        self.lineEdit_maxtokens_title.setObjectName("lineEdit_maxtokens_title")
        self.verticalLayout_7.addWidget(self.lineEdit_maxtokens_title)
        self.lineEdit_tokens = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_tokens.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.lineEdit_tokens.setObjectName("lineEdit_tokens")
        self.verticalLayout_7.addWidget(self.lineEdit_tokens)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: transparent;")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.lineEdit_rounds = QtWidgets.QLineEdit(parent=self.tab_model)
        self.lineEdit_rounds.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_rounds.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.lineEdit_rounds.setText("")
        self.lineEdit_rounds.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_rounds.setObjectName("lineEdit_rounds")
        self.horizontalLayout_6.addWidget(self.lineEdit_rounds)
        self.horizontalSlider_rounds = QtWidgets.QSlider(parent=self.tab_model)
        self.horizontalSlider_rounds.setProperty("value", 0)
        self.horizontalSlider_rounds.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_rounds.setObjectName("horizontalSlider_rounds")
        self.horizontalLayout_6.addWidget(self.horizontalSlider_rounds)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_model, "")
        self.tab_chat = QtWidgets.QWidget()
        self.tab_chat.setObjectName("tab_chat")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_chat)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(parent=self.tab_chat)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_prompt_title = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_prompt_title.setStyleSheet("background-color: transparent;")
        self.lineEdit_prompt_title.setFrame(False)
        self.lineEdit_prompt_title.setReadOnly(True)
        self.lineEdit_prompt_title.setObjectName("lineEdit_prompt_title")
        self.verticalLayout_2.addWidget(self.lineEdit_prompt_title)
        self.plainTextEdit_prompt = QtWidgets.QPlainTextEdit(parent=self.widget_2)
        self.plainTextEdit_prompt.setMaximumSize(QtCore.QSize(16777215, 200))
        self.plainTextEdit_prompt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit_prompt.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit_prompt.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.plainTextEdit_prompt.setObjectName("plainTextEdit_prompt")
        self.verticalLayout_2.addWidget(self.plainTextEdit_prompt, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab_chat, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=settings_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settings_dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(settings_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(settings_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(settings_dialog)

    def retranslateUi(self, settings_dialog):
        _translate = QtCore.QCoreApplication.translate
        settings_dialog.setWindowTitle(_translate("settings_dialog", "设置"))
        self.lineEdit_AI.setText(_translate("settings_dialog", "AI模型提供方"))
        self.lineEdit_api_key_title.setText(_translate("settings_dialog", "API Key"))
        self.lineEdit_key.setPlaceholderText(_translate("settings_dialog", "API Key"))
        self.lineEdit_model_title.setText(_translate("settings_dialog", "模型"))
        self.lineEdit_maxtokens_title.setText(_translate("settings_dialog", "最大tokens"))
        self.lineEdit_tokens.setPlaceholderText(_translate("settings_dialog", "Max Tokens"))
        self.lineEdit.setText(_translate("settings_dialog", "限制上下文最大回合数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_model), _translate("settings_dialog", "模型"))
        self.lineEdit_prompt_title.setText(_translate("settings_dialog", "你希望给AI的提示"))
        self.plainTextEdit_prompt.setPlaceholderText(_translate("settings_dialog", "新对话的默认提示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_chat), _translate("settings_dialog", "对话"))
