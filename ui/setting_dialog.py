import json

from PyQt6.QtCore import QByteArray
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog

import config
import pydb
from ui.settings_dialog_ui import Ui_settings_dialog

# 读取json文件
with open('./pc.json', "r", encoding='utf-8') as f:
    json_data = json.load(f)


class SettingDialog(QDialog, Ui_settings_dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_key.setText(config.openai.api_key)
        self.comboBox_model.setCurrentText(config.openai.model)
        self.lineEdit_tokens.setText(str(config.openai.max_tokens))
        self.lineEdit_rounds.setText(str(config.openai.chat_rounds))
        self.plainTextEdit_prompt.setPlainText(config.openai.chat_prompt)
        # 信号槽连接
        self.lineEdit_rounds.textChanged.connect(self.on_rounds_edit_changed)
        self.horizontalSlider_rounds.valueChanged.connect(self.on_rounds_slider_changed)
        self.comboBox_province.currentIndexChanged.connect(self.on_province_combobox_changed)
        self.add_to_combobox()

        self.current_user = None

    def accept(self):
        config.openai.api_key = self.lineEdit_key.text()
        config.openai.model = self.comboBox_model.currentText()
        config.openai.max_tokens = int(self.lineEdit_tokens.text())
        config.openai.chat_rounds = int(self.lineEdit_rounds.text())
        config.openai.chat_prompt = self.plainTextEdit_prompt.toPlainText()
        if self.current_user != "未登录":
            pydb.up_one_date("users", "username", self.lineEdit_nickname.text(), int(self.lineEdit_id.text()))
            pydb.up_one_date("users", "province", self.comboBox_province.currentText(), int(self.lineEdit_id.text()))
            pydb.up_one_date("users", "city", self.comboBox_city.currentText(), int(self.lineEdit_id.text()))
            if self.radioButton_male.isChecked():
                pydb.up_one_date("users", "sex", "M", int(self.lineEdit_id.text()))
            else:
                pydb.up_one_date("users", "sex", "FM", int(self.lineEdit_id.text()))

        config.event1.set()
        config.event1.clear()
        self.close()

    def on_rounds_edit_changed(self):
        if self.lineEdit_rounds.text() != '':
            self.horizontalSlider_rounds.setValue(int(self.lineEdit_rounds.text()))

    def on_rounds_slider_changed(self):
        self.lineEdit_rounds.setText(str(self.horizontalSlider_rounds.value()))

    def set_user_information(self, username):
        self.current_user = username
        if username == "未登录":
            return
        self.lineEdit_id.setText(str(pydb.select_one_date("id", "users", "username", username)))
        self.lineEdit_nickname.setText(str(pydb.select_one_date("username", "users", "username", username)))
        if pydb.select_one_date("sex", "users", "username", username) == 'M':
            self.radioButton_male.setChecked(True)
        else:
            self.radioButton_female.setChecked(True)
        self.comboBox_city.setCurrentText(str(pydb.select_one_date("city", "users", "username", username)))
        self.comboBox_province.setCurrentText(str(pydb.select_one_date("province", "users", "username", username)))
        byte_array = QByteArray(pydb.select_one_date("avatar", "users", "username", username))
        # 从QByteArray加载图片到QPixmap
        pixmap = QPixmap()
        pixmap.loadFromData(byte_array)
        self.label_icon.setPixmap(pixmap)

    def add_to_combobox(self):
        # 遍历json数据
        for key, value in json_data.items():
            # 将每个项添加到comboBox中
            self.comboBox_province.addItem(key)

    def on_province_combobox_changed(self):
        province = self.comboBox_province.currentText()
        self.comboBox_city.clear()
        for value in json_data[province]:
            self.comboBox_city.addItem(value)
