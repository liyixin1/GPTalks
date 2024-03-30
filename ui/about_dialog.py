from PyQt6.QtWidgets import QDialog

from ui.about_dialog_ui import Ui_about_dialog


class AboutDialog(QDialog, Ui_about_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

