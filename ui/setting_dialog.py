from PyQt6.QtWidgets import QDialog

from chatgpt import chatgpt
from config import openai
from ui.settings_dialog_ui import Ui_settings_dialog


class SettingDialog(QDialog, Ui_settings_dialog):
    def __init__(self):
        super().__init__()

        self.chat_prompt = None
        self.rounds = None
        self.max_tokens = None
        self.model = None
        self.api_key = None
        self.setupUi(self)

        self.plainTextEdit_api_key.setPlainText(openai.api_key)
        self.plainTextEdit_model.setPlainText(openai.model)
        self.plainTextEdit_maxtokens.setPlainText(str(openai.max_tokens))
        self.lineEdit_rounds.setText(str(openai.chat_rounds))
        self.plainTextEdit_prompt.setPlainText(openai.chat_prompt)

        self.lineEdit_rounds.textChanged.connect(self.on_rounds_edit_changed)
        self.horizontalSlider_rounds.valueChanged.connect(self.on_rounds_slider_changed)

    def accept(self):
        self.api_key = self.plainTextEdit_api_key.toPlainText()
        self.model = self.plainTextEdit_model.toPlainText()
        self.max_tokens = (self.plainTextEdit_maxtokens.toPlainText())
        self.rounds = self.lineEdit_rounds.text()
        self.chat_prompt = self.plainTextEdit_prompt.toPlainText()

        openai.get_gpt_parameter(self.api_key, self.model, self.max_tokens, self.rounds, self.chat_prompt)
        openai.write_to_config(self.model, self.max_tokens, self.rounds, self.chat_prompt)
        chatgpt.set_gpt_parameter()
        self.close()

    def on_rounds_edit_changed(self):
        if self.lineEdit_rounds.text() != '':
            self.horizontalSlider_rounds.setValue(int(self.lineEdit_rounds.text()))

    def on_rounds_slider_changed(self):
        self.lineEdit_rounds.setText(str(self.horizontalSlider_rounds.value()))
