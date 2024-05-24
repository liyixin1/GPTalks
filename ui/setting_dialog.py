import json

from PyQt6.QtWidgets import QDialog

import config
import pydb
from ui.settings_dialog_ui import Ui_settings_dialog

# 读取json文件
with open('./pc.json', "r", encoding='utf-8') as f:
    json_province_city = json.load(f)
with open('./ai_model.json', "r", encoding='utf-8') as f:
    json_ai_model = json.load(f)


class SettingDialog(QDialog, Ui_settings_dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_to_combobox_province()
        self.add_to_combobox_ai()

        self.lineEdit_key.setText(config.aimodel.api_key)
        self.lineEdit_tokens.setText(str(config.aimodel.max_tokens))
        self.lineEdit_rounds.setText(str(config.aimodel.chat_rounds))
        self.horizontalSlider_rounds.setValue(config.aimodel.chat_rounds)
        self.plainTextEdit_prompt.setPlainText(config.aimodel.chat_prompt)
        # 信号槽连接
        self.lineEdit_rounds.textChanged.connect(self.on_rounds_edit_changed)
        self.horizontalSlider_rounds.valueChanged.connect(self.on_rounds_slider_changed)
        self.comboBox_province.currentIndexChanged.connect(self.on_province_combobox_changed)
        self.comboBox_AI.currentIndexChanged.connect(self.on_ai_combobox_changed)

        self.comboBox_AI.setCurrentText(config.aimodel.ai)
        self.on_ai_combobox_changed()
        self.comboBox_model.setCurrentText(config.aimodel.model)

        self.current_user = None

    def accept(self):
        config.aimodel.ai = self.comboBox_AI.currentText()
        config.aimodel.api_key = self.lineEdit_key.text()
        config.aimodel.model = self.comboBox_model.currentText()
        config.aimodel.max_tokens = int(self.lineEdit_tokens.text())
        config.aimodel.chat_rounds = int(self.lineEdit_rounds.text())
        config.aimodel.chat_prompt = self.plainTextEdit_prompt.toPlainText()
        if self.current_user != "未登录":
            pydb.up_one_date("users", "username", self.lineEdit_nickname.text(), "id", self.lineEdit_id.text())
            pydb.up_one_date("users", "province", self.comboBox_province.currentText(), "id", self.lineEdit_id.text())
            pydb.up_one_date("users", "city", self.comboBox_city.currentText(), "id", self.lineEdit_id.text())
            if self.radioButton_male.isChecked():
                pydb.up_one_date("users", "sex", "M", "id", self.lineEdit_id.text())
            else:
                pydb.up_one_date("users", "sex", "FM", "id", self.lineEdit_id.text())

            pydb.up_one_date("ai", "ai", self.comboBox_AI.currentText(), "name", self.lineEdit_nickname.text())
            pydb.up_one_date("ai", "model", self.comboBox_model.currentText(), "name", self.lineEdit_nickname.text())
            # pydb.up_one_date("ai", "key", self.lineEdit_key.text(), "name", self.lineEdit_nickname.text())
            pydb.up_one_date("ai", "rounds", self.lineEdit_rounds.text(), "name", self.lineEdit_nickname.text())
            pydb.up_one_date("ai", "max_tokens", self.lineEdit_tokens.text(), "name", self.lineEdit_nickname.text())
            pydb.up_one_date("ai", "chat_prompt", self.plainTextEdit_prompt.toPlainText(), "name", self.lineEdit_nickname.text())

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
        self.comboBox_province.setCurrentText(str(pydb.select_one_date("province", "users", "username", username)))
        self.on_province_combobox_changed()
        self.comboBox_city.setCurrentText(str(pydb.select_one_date("city", "users", "username", username)))

    def add_to_combobox_province(self):
        # 遍历json数据
        for key, value in json_province_city.items():
            # 将每个项添加到comboBox中
            self.comboBox_province.addItem(key)

    def on_province_combobox_changed(self):
        province = self.comboBox_province.currentText()
        self.comboBox_city.clear()
        for value in json_province_city[province]:
            self.comboBox_city.addItem(value)

    def add_to_combobox_ai(self):
        for key, value in json_ai_model.items():
            self.comboBox_AI.addItem(key)

    def on_ai_combobox_changed(self):
        ai = self.comboBox_AI.currentText()
        self.comboBox_model.clear()
        for value in json_ai_model[ai]:
            self.comboBox_model.addItem(value)
