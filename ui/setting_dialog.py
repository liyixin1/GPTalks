import json

from PyQt6.QtWidgets import QDialog

import config
from ui.settings_dialog_ui import Ui_settings_dialog

# 读取json文件
with open('./ai_model.json', "r", encoding='utf-8') as f:
    json_ai_model = json.load(f)


class SettingDialog(QDialog, Ui_settings_dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_to_combobox_ai()

        self.lineEdit_key.setText(config.aimodel.api_key)
        self.lineEdit_tokens.setText(str(config.aimodel.max_tokens))
        self.lineEdit_rounds.setText(str(config.aimodel.chat_rounds))
        self.horizontalSlider_rounds.setValue(config.aimodel.chat_rounds)
        self.plainTextEdit_prompt.setPlainText(config.aimodel.chat_prompt)
        # 信号槽连接
        self.lineEdit_rounds.textChanged.connect(self.on_rounds_edit_changed)
        self.horizontalSlider_rounds.valueChanged.connect(self.on_rounds_slider_changed)
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
        config.event1.set()
        config.event1.clear()
        self.close()

    def on_rounds_edit_changed(self):
        if self.lineEdit_rounds.text() != '':
            self.horizontalSlider_rounds.setValue(int(self.lineEdit_rounds.text()))

    def on_rounds_slider_changed(self):
        self.lineEdit_rounds.setText(str(self.horizontalSlider_rounds.value()))

    def add_to_combobox_ai(self):
        for key, value in json_ai_model.items():
            self.comboBox_AI.addItem(key)

    def on_ai_combobox_changed(self):
        ai = self.comboBox_AI.currentText()
        self.comboBox_model.clear()
        for value in json_ai_model[ai]:
            self.comboBox_model.addItem(value)
