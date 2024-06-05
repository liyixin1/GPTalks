"""
about_dialog.py
关于窗口，展示应用程序或开发者信息
"""
from PyQt6.QtWidgets import QDialog
from ui.about_dialog_ui import Ui_about_dialog


class AboutDialog(QDialog, Ui_about_dialog):
    """主类"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
