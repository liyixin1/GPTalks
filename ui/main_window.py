"""
main_windows.py
应用程序的主界面，集成了多种功能，包括处理文本输入、音频输入，以及会话管理等。
"""
import base64
from concurrent.futures import ThreadPoolExecutor
import re
from PyQt6 import QtWidgets
from PyQt6.QtCore import QObject, pyqtSignal, Qt, QEvent, QBuffer, QIODevice
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from list_widget_item import ListWidgetItem
from ui.about_dialog import AboutDialog
from ui.plain_text_edit import MyPlainTextEdit
from ui.setting_dialog import SettingDialog
from ui.main_window_ui import Ui_MainWindow


class Communicate(QObject):
    """定义信号"""
    text_ready = pyqtSignal(tuple)
    input_clear = pyqtSignal()
    error_handling = pyqtSignal(str)


class MainWindow(QMainWindow, Ui_MainWindow):
    """主界面类"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_dialog = SettingDialog()
        self.about_dialog = AboutDialog()
        self.base64_image = None
        self.current_theme = None
        self.icons = {
            'text': QIcon('ui/images/new_text.png'),
            'button_send': QIcon('ui/images/send.svg'),
            'button_upload': QIcon('ui/images/upload.svg'),
            'button_add': QIcon('ui/images/add.svg'),
            'button_delete': QIcon('ui/images/delete.svg'),
            'button_settings': QIcon('ui/images/settings.svg'),
            'button_about': QIcon('ui/images/about.svg'),
            'window_logo': QIcon('ui/images/window_logo.png'),
        }

        self.verticalLayout_6.removeWidget(self.plainTextEdit_input)
        self.plainTextEdit_input = MyPlainTextEdit()
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")
        self.verticalLayout_6.addWidget(self.plainTextEdit_input)

        # 连接信号与槽
        self.pushButton_send.clicked.connect(self.on_send_button_clicked)
        self.listWidget_session.currentItemChanged.connect(self.on_current_item_changed)
        self.pushButton_new_chat.clicked.connect(self.on_new_chat_button_clicked)
        self.pushButton_delete.clicked.connect(self.on_delete_button_clicked)
        self.lineEdit_name.editingFinished.connect(self.on_session_name_editing_finished)
        self.pushButton_settings.clicked.connect(self.on_setting_button_clicked)
        self.pushButton_about.clicked.connect(self.on_about_button_clicked)
        self.plainTextEdit_input.ctrlEnterPressed.connect(self.on_send_button_clicked)
        self.pushButton_upload.clicked.connect(self.on_upload_button_clicked)
        self.plainTextEdit_input.textChanged.connect(self.changed_send_button_state)

        # 创建信号类对象
        self.communicate = Communicate()
        # 用于线程安全GUI更新的通信
        self.communicate.text_ready.connect(self.update_text_browser)
        self.communicate.input_clear.connect(self.clear_input)
        self.communicate.error_handling.connect(self.error_handling)
        self.settings_dialog.themeChanged.connect(self.changed_theme)
        self.settings_dialog.fontSizeChanged.connect(self.changed_font_size)
        # 安装事件过滤器
        self.label_image.installEventFilter(self)
        # 初始化状态
        self.changed_send_button_state()
        self.changed_theme(self.settings_dialog.ComboBox_theme.currentText())
        self.pushButton_send.setIcon(self.icons['button_send'])
        self.pushButton_upload.setIcon(self.icons['button_upload'])
        self.pushButton_delete.setIcon(self.icons['button_delete'])
        self.pushButton_settings.setIcon(self.icons['button_settings'])
        self.pushButton_about.setIcon(self.icons['button_about'])
        self.pushButton_new_chat.setIcon(self.icons['button_add'])
        self.setWindowIcon(self.icons['window_logo'])

    # 发送按钮处理模块--------------------------------------------------↓
    def on_send_button_clicked(self):
        """处理发送按钮点击事件，即将输入的文本记录到当前选中的会话中。"""
        if self.plainTextEdit_input.toPlainText() == "":
            return
        executor = ThreadPoolExecutor(max_workers=1)
        self.pushButton_delete.setEnabled(False)
        current_item = self.listWidget_session.currentItem()
        if self.listWidget_session.count() == 0:  # 如果当前不存在会话记录，则新建一个
            self.on_new_chat_button_clicked()
            current_item = self.listWidget_session.currentItem()  # 捕获当前对话项
        executor.submit(self._commit_button_clicked_task, current_item)

    def _commit_button_clicked_task(self, current_item):
        """单击提交按钮时运行的实际任务。"""
        input_text = self.plainTextEdit_input.toPlainText()
        self.communicate.input_clear.emit()
        text = self.listWidget_session.currentItem().get_record(
            input_text,
            self.base64_image,
            self.listWidget_session.currentItem().text(),
        )
        if text.get('Error') is not None:
            self.communicate.error_handling.emit(text.get('Error'))
        else:
            self.communicate.text_ready.emit((current_item, text['OK']))
            self.base64_image = None

    def update_text_browser(self, item_text_pair):
        """用新的文本更新QTextBrowser。"""
        # 记录当前滚动位置
        ver_scrollbar = self.textBrowser_show.verticalScrollBar()
        hor_scrollbar = self.textBrowser_show.horizontalScrollBar()
        ver_value = ver_scrollbar.value()
        hor_value = hor_scrollbar.value()
        item, text = item_text_pair
        if self.listWidget_session.currentItem() == item:
            self.textBrowser_show.setHtml(text)
        # 还原滚动位置
        ver_scrollbar.setValue(ver_value)
        hor_scrollbar.setValue(hor_value)
        self.pushButton_delete.setEnabled(True)

    def clear_input(self):
        """清除输入框内容"""
        self.plainTextEdit_input.clear()
        self.label_image.clear()

    def error_handling(self, e):
        """错误处理"""
        QtWidgets.QMessageBox.warning(self, "警告", f"出现错误,请检查:\n {str(e)}")

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

    def on_new_chat_button_clicked(self):
        """新建一个文本对话项，并自动选中这个新对话项。"""
        new_item = ListWidgetItem("对话" + str(self.listWidget_session.count() + 1))
        new_item.setIcon(self.icons.get('text'))
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
        self.settings_dialog.show()

    def on_about_button_clicked(self):
        """显示关于窗口"""
        self.about_dialog.exec()

    def on_upload_button_clicked(self):
        """选取本地图片"""
        current_model = ListWidgetItem.get_current_model(self.listWidget_session.currentItem())
        if current_model in ('gpt-4-turbo', 'gpt-4o'):
            self.pushButton_upload.setToolTip("支持上传1张图片\n最大20MB")
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, "选择图片", "",
                                                       "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif)")

            if file_path:
                # 加载并显示图片
                pixmap = QPixmap(file_path)
                self.label_image.setPixmap(pixmap)
                self.label_image.setScaledContents(True)  # 让图片适应标签大小

                # 加载图片
                image = QImage(file_path)
                # 创建缓冲区并保存图片数据
                buffer = QBuffer()
                # 打开缓冲区，准备写入
                buffer.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Truncate)
                # 保存图片为 JPEG 格式到缓冲区
                if image.save(buffer, "JPEG"):
                    # 获取 base64 编码的图片数据
                    self.base64_image = base64.b64encode(buffer.data()).decode('utf-8')
                # 关闭缓冲区
                buffer.close()
        else:
            self.pushButton_upload.setToolTip("当前模型不支持上传图片！")

    # pylint: disable=invalid-name
    def eventFilter(self, obj, event):
        """定义点击label事件，点中Label对象即删除其中图片"""
        if obj == self.label_image:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.label_image.setPixmap(QPixmap())  # 清除图片
                    return True  # 事件已被处理，不再传递
        return super().eventFilter(obj, event)

    def changed_theme(self, current_theme):
        """界面主题变动槽"""
        if current_theme == '浅色模式':
            self.current_theme = 'Light Mode'
        elif current_theme == '深色模式':
            self.current_theme = 'Dark Mode'
        self.loadStyleSheet(self.current_theme)

    def loadStyleSheet(self, stylesheet):
        """更换加载样式表"""
        qss = ''
        if stylesheet == "Light Mode":
            with open('qss/main_style_light.qss', 'r', encoding='utf-8') as f:
                qss = f.read()
        elif stylesheet == "Dark Mode":
            with open('qss/main_style_dark.qss', 'r', encoding='utf-8') as f:
                qss = f.read()
        self.setStyleSheet(qss)

    def changed_font_size(self, current_font_size):
        """界面字体大小变动对应槽"""
        self.modifyStylesheet(current_font_size)

    def modifyStylesheet(self, fontsize):
        """更新字体大小"""
        stylesheet = ['qss/main_style_light.qss', 'qss/main_style_dark.qss']
        for i in stylesheet:
            with open(i, 'r', encoding='utf-8') as f:
                stylesheet_r = f.read()
            # 使用正则表达式修改字体大小
            new_stylesheet_r = re.sub(r'font-size: \d+px;',
                                      f'font-size: {fontsize}px;',
                                      stylesheet_r)
            with open(i, 'w', encoding='utf-8') as f:
                f.write(new_stylesheet_r)
        self.loadStyleSheet(self.current_theme)

    def changed_send_button_state(self):
        """当输入为空时禁用发送按钮"""
        if self.plainTextEdit_input.toPlainText() != "":
            self.pushButton_send.setEnabled(True)
        else:
            self.pushButton_send.setEnabled(False)
