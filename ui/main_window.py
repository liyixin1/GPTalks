from PyQt6.QtWidgets import QMainWindow

from list_widget_Item import ListWidgetItem
from ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_commit.clicked.connect(self.on_commit_button_clicked)
        self.listWidget_session.currentItemChanged.connect(self.on_current_item_changed)

        list_item = ListWidgetItem("会话1")
        list_item_2 = ListWidgetItem("会话2")
        self.listWidget_session.addItem(list_item)
        self.listWidget_session.addItem(list_item_2)
        self.listWidget_session.setCurrentItem(list_item)

    def on_commit_button_clicked(self):
        self.textBrowser_show.setText(
            self.listWidget_session.currentItem().get_record(self.plainTextEdit_input.toPlainText()))
        self.plainTextEdit_input.clear()

    def on_current_item_changed(self):
        self.lineEdit_name.setText(self.listWidget_session.currentItem().text())
