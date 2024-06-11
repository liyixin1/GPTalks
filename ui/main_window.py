"""
main_windows.py
应用程序的主界面，集成了多种功能，包括处理文本输入、音频输入，以及会话管理等。
"""
from concurrent.futures import ThreadPoolExecutor
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from list_widget_item import ListWidgetItem
from ui.about_dialog import AboutDialog
from ui.plain_text_edit import MyPlainTextEdit
from ui.setting_dialog import SettingDialog
from ui.main_window_ui import Ui_MainWindow


class Communicate(QObject):
    """定义信号"""
    text_ready = pyqtSignal(tuple)
    input_clear = pyqtSignal()


class MainWindow(QMainWindow, Ui_MainWindow):
    """主界面类"""
    def __init__(self):
        super().__init__()
        self.settings_dialog = None
        self.about_dialog = None
        self.setupUi(self)

        self.horizontalLayout_4.removeWidget(self.plainTextEdit_input)
        self.plainTextEdit_input = MyPlainTextEdit()
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")

        # 通过remove将按钮拿出来，先添加输入框再添加按钮，使其相对位置不变
        self.horizontalLayout_4.removeItem(self.verticalLayout_2)
        self.horizontalLayout_4.addWidget(self.plainTextEdit_input)
        self.horizontalLayout_4.addItem(self.verticalLayout_2)
        # -------------------------------------------------------

        # 连接信号与槽
        self.pushButton_send.clicked.connect(self.on_send_button_clicked)
        self.listWidget_session.currentItemChanged.connect(self.on_current_item_changed)
        self.pushButton_new.clicked.connect(self.on_new_button_clicked)
        self.pushButton_delect.clicked.connect(self.on_delete_button_clicked)
        self.lineEdit_name.editingFinished.connect(self.on_session_name_editing_finished)
        self.pushButton_settings.clicked.connect(self.on_setting_button_clicked)
        self.pushButton_about.clicked.connect(self.on_about_button_clicked)
        self.plainTextEdit_input.ctrlEnterPressed.connect(self.on_send_button_clicked)
        # -------------------------------------------------------
        self.current_model = None

        # 用于线程安全GUI更新的通信对象
        self.communicate = Communicate()
        self.communicate.text_ready.connect(self.update_text_browser)
        self.communicate.input_clear.connect(self.clear_input)

    # 发送按钮处理模块--------------------------------------------------↓
    def on_send_button_clicked(self):
        """处理发送按钮点击事件，即将输入的文本记录到当前选中的会话中。"""
        executor = ThreadPoolExecutor(max_workers=1)
        self.pushButton_delect.setEnabled(False)
        current_item = self.listWidget_session.currentItem()
        if self.listWidget_session.count() == 0:  # 如果当前不存在会话记录，则新建一个
            self.on_new_button_clicked()
            current_item = self.listWidget_session.currentItem()    # 捕获当前对话项
        executor.submit(self._commit_button_clicked_task, current_item)

    def _commit_button_clicked_task(self, current_item):
        """单击提交按钮时运行的实际任务。"""
        input_text = self.plainTextEdit_input.toPlainText()
        self.communicate.input_clear.emit()
        text = self.listWidget_session.currentItem().get_record(
            input_text,
            self.listWidget_session.currentItem().text(),
            self,
        )
        self.communicate.text_ready.emit((current_item, text))

    def update_text_browser(self, item_text_pair):
        """用新的文本更新QTextBrowser。"""
        item, text = item_text_pair
        if self.listWidget_session.currentItem() == item:
            self.textBrowser_show.setHtml(text)
        self.pushButton_delect.setEnabled(True)

    def clear_input(self):
        """清除输入框内容"""
        self.plainTextEdit_input.clear()
    # 发送按钮处理模块--------------------------------------------------↑

    def on_current_item_changed(self):
        """当选中的对话项发生变化时，更新相应的对话名称和对话显示。"""
        if self.listWidget_session.currentItem() is None:
            self.lineEdit_name.setText("")
            self.textBrowser_show.setHtml("")
        else:
            self.lineEdit_name.setText(self.listWidget_session.currentItem().text())
            self.textBrowser_show.setHtml(
                self.listWidget_session.currentItem().record_to_display_text())

    def on_new_button_clicked(self):
        """新建一个会话项，并自动选中这个新会话项。"""
        new_item = ListWidgetItem("对话" + str(self.listWidget_session.count() + 1))
        self.listWidget_session.addItem(new_item)
        self.listWidget_session.setCurrentItem(new_item)

    def on_delete_button_clicked(self):
        """删除当前选中的会话项。"""
        del_item = self.listWidget_session.takeItem(self.listWidget_session.currentRow())
        del del_item

    def on_session_name_editing_finished(self):
        """会话名称编辑完成后，更新当前会话项的显示名称。"""
        if self.listWidget_session.count() != 0:
            self.listWidget_session.currentItem().setText(self.lineEdit_name.text())

    def on_setting_button_clicked(self):
        """显示设置窗口。"""
        self.settings_dialog = SettingDialog()
        self.settings_dialog.show()

    def on_about_button_clicked(self):
        """显示关于窗口"""
        self.about_dialog = AboutDialog()
        self.about_dialog.exec()
