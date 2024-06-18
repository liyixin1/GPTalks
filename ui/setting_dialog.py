"""
setting_dialog.py
设置界面后端逻辑，实现调整应用程序的行为和参数
"""
import json
from PyQt6.QtWidgets import QDialog
import config
from ui.settings_dialog_ui import Ui_settings_dialog

with open('./ai_model.json', "r", encoding='utf-8') as f:
    json_ai_model = json.load(f)


class SettingDialog(QDialog, Ui_settings_dialog):
    """继承GUI类，初始化界面并加载配置"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_to_combobox_ai()

        self.lineEdit_key.setText(config.aimodel.api_key)
        # max tokens
        self.lineEdit_tokens.setText(str(config.aimodel.max_tokens))
        self.horizontalSlider_tokens.setValue(config.aimodel.max_tokens)
        # 上下文记忆数
        self.lineEdit_rounds.setText(str(config.aimodel.chat_rounds))
        self.horizontalSlider_rounds.setValue(config.aimodel.chat_rounds)

        self.plainTextEdit_prompt.setPlainText(config.aimodel.chat_prompt)
        # 信号槽连接
        self.lineEdit_rounds.textChanged.connect(self.on_rounds_edit_changed)
        self.horizontalSlider_rounds.valueChanged.connect(self.on_rounds_slider_changed)

        self.lineEdit_tokens.textChanged.connect(self.on_tokens_edit_changed)
        self.horizontalSlider_tokens.valueChanged.connect(self.on_tokens_slider_changed)

        self.comboBox_AI.currentIndexChanged.connect(self.on_ai_combobox_changed)

        self.comboBox_AI.setCurrentText(config.aimodel.ai)
        self.on_ai_combobox_changed()
        self.comboBox_model.setCurrentText(config.aimodel.model)

        self.current_user = None

    def accept(self):
        """重写按下确定按钮信号的槽，修改当前的配置并发送信号到config.write_to_config()"""
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
        """连续对话回合数改变信号对应槽，当数值修改时，滑块同步变动"""
        if self.lineEdit_rounds.text() != '':
            self.horizontalSlider_rounds.setValue(int(self.lineEdit_rounds.text()))

    def on_rounds_slider_changed(self):
        """连续对话回合数滑块变动信号对应槽，当滑块滑动时，数字同步变化"""
        self.lineEdit_rounds.setText(str(self.horizontalSlider_rounds.value()))

    def on_tokens_edit_changed(self):
        """最大tokens数改变信号对应槽，当数值修改时，滑块同步变动"""
        if self.lineEdit_tokens.text() != '':
            self.horizontalSlider_tokens.setValue(int(self.lineEdit_tokens.text()))

    def on_tokens_slider_changed(self):
        """最大tokens滑块变动信号对应槽，当滑块滑动时，数字同步变化"""
        self.lineEdit_tokens.setText(str(self.horizontalSlider_tokens.value()))

    def add_to_combobox_ai(self):
        """初始化时加载展示模型"""
        for key in json_ai_model:
            self.comboBox_AI.addItem(key)

    def on_ai_combobox_changed(self):
        """模型提供方变化信号对应槽，当选择了其他模型提供方时，模型参数同步变化到改提供方提供的模型"""
        ai = self.comboBox_AI.currentText()
        self.comboBox_model.clear()
        for value in json_ai_model[ai]:
            self.comboBox_model.addItem(value)
