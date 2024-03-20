from PyQt6.QtWidgets import QMainWindow

from list_widget_Item import ListWidgetItem
from ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_commit.clicked.connect(self.on_commit_button_clicked)  # 提交按钮点击信号
        self.listWidget_session.currentItemChanged.connect(self.on_current_item_changed)  # 鼠标点击会话列表项信号
        self.pushButton_new.clicked.connect(self.on_new_button_clicked)  # 新建会话按钮点击信号
        self.pushButton_delect.clicked.connect(self.on_delect_button_clicked)  # 删除会话按钮点击信号

    def on_commit_button_clicked(self):
        if self.listWidget_session.count() == 0:  # 如果当前不存在会话记录，则新建一个
            self.on_new_button_clicked()
        self.textBrowser_show.setText(
            self.listWidget_session.currentItem().get_record(self.plainTextEdit_input.toPlainText()))
        self.plainTextEdit_input.clear()

    def on_current_item_changed(self):
        self.lineEdit_name.setText(self.listWidget_session.currentItem().text())
        self.textBrowser_show.setText(self.listWidget_session.currentItem().record_to_display_text())

    def on_new_button_clicked(self):
        new_item = ListWidgetItem("会话" + str(self.listWidget_session.count() + 1))
        self.listWidget_session.addItem(new_item)
        self.listWidget_session.setCurrentItem(new_item)

    def on_delect_button_clicked(self):
        del_item = self.listWidget_session.takeItem(self.listWidget_session.currentRow())
        del del_item
