from PyQt6.QtWidgets import QDialog

import config
from ui.settings_dialog_ui import Ui_settings_dialog


class SettingDialog(QDialog, Ui_settings_dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plainTextEdit_api_key.setPlainText(config.openai.api_key)
        self.plainTextEdit_model.setPlainText(config.openai.model)
        self.plainTextEdit_maxtokens.setPlainText(str(config.openai.max_tokens))
        self.lineEdit_rounds.setText(str(config.openai.chat_rounds))
        self.plainTextEdit_prompt.setPlainText(config.openai.chat_prompt)

        self.lineEdit_rounds.textChanged.connect(self.on_rounds_edit_changed)
        self.horizontalSlider_rounds.valueChanged.connect(self.on_rounds_slider_changed)

    def accept(self):
        config.openai.api_key = self.plainTextEdit_api_key.toPlainText()
        config.openai.model = self.plainTextEdit_model.toPlainText()
        config.openai.max_tokens = self.plainTextEdit_maxtokens.toPlainText()
        config.openai.chat_rounds = int(self.lineEdit_rounds.text())
        print(config.openai.chat_rounds)
        config.openai.chat_prompt = self.plainTextEdit_prompt.toPlainText()
        config.event.set()
        config.event.clear()
        self.close()

    def on_rounds_edit_changed(self):
        if self.lineEdit_rounds.text() != '':
            self.horizontalSlider_rounds.setValue(int(self.lineEdit_rounds.text()))

    def on_rounds_slider_changed(self):
        self.lineEdit_rounds.setText(str(self.horizontalSlider_rounds.value()))
