from PyQt6.QtWidgets import QMainWindow

from list_widget_Item import ListWidgetItem
from ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_commit.clicked.connect(self.on_commit_button_clicked)
        list_item = ListWidgetItem("会话1")
        self.listWidget_session.addItem(list_item)
        self.listWidget_session.setCurrentItem(list_item)

    def on_commit_button_clicked(self):
        self.textBrowser_show.setText(
            self.listWidget_session.currentItem().get_record(self.plainTextEdit_input.toPlainText()))
        self.plainTextEdit_input.clear()
