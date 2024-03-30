import threading
import time

import pyaudio
from PyQt6.QtWidgets import QMainWindow, QDialog

from list_widget_Item import ListWidgetItem
from speech_recognition import SpeechRecognition
from ui.about_dialog import AboutDialog
from ui.about_dialog_ui import Ui_about_dialog
from ui.plain_text_edit import MyPlainTextEdit
from ui.setting_dialog import SettingDialog
from ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.settings_dialog = None
        self.about_dialog = None
        self.setupUi(self)
        self.horizontalLayout_4.removeWidget(self.plainTextEdit_input)
        self.plainTextEdit_input = MyPlainTextEdit(parent=self.layoutWidget_4)
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")
        # 通过remove将按钮拿出来，先添加输入框再添加按钮，使其相对位置不变
        self.horizontalLayout_4.removeItem(self.verticalLayout_2)
        self.horizontalLayout_4.addWidget(self.plainTextEdit_input)
        self.horizontalLayout_4.addItem(self.verticalLayout_2)
        # -------------------------------------------------------

        self.pushButton_commit.clicked.connect(self.on_commit_button_clicked)  # 提交按钮点击信号
        self.listWidget_session.currentItemChanged.connect(self.on_current_item_changed)  # 鼠标点击会话列表项信号
        self.pushButton_new.clicked.connect(self.on_new_button_clicked)  # 新建会话按钮点击信号
        self.pushButton_delect.clicked.connect(self.on_delete_button_clicked)  # 删除会话按钮点击信号
        self.lineEdit_name.editingFinished.connect(self.on_session_name_editing_finished)
        self.pushButton_settings.clicked.connect(self.on_setting_button_clicked)
        self.pushButton_about.clicked.connect(self.on_about_button_clicked)
        self.plainTextEdit_input.ctrlEnterPressed.connect(self.on_commit_button_clicked)
        self.pushButton_audio.toggled.connect(self.on_audio_button_toggled)

        # 录音参数设置
        self.for_mat = pyaudio.paInt16  # 音频格式
        self.channels = 1  # 单声道
        self.rate = 16000  # 采样率
        self.chunk = 1024  # 每次读取的音频流长度
        self.isSwitchOn = False

    def on_commit_button_clicked(self):
        if self.listWidget_session.count() == 0:  # 如果当前不存在会话记录，则新建一个
            self.on_new_button_clicked()
        self.textBrowser_show.setText(
            self.listWidget_session.currentItem().get_record(
                self.plainTextEdit_input.toPlainText(),
                self.listWidget_session.currentItem().text()
            )
        )
        self.plainTextEdit_input.clear()

    def on_current_item_changed(self):
        if self.listWidget_session.currentItem() is None:
            self.lineEdit_name.setText("")
            self.textBrowser_show.setText("")
        else:
            self.lineEdit_name.setText(self.listWidget_session.currentItem().text())
            self.textBrowser_show.setHtml(self.listWidget_session.currentItem().record_to_display_text())

    def on_new_button_clicked(self):
        new_item = ListWidgetItem("会话" + str(self.listWidget_session.count() + 1))
        self.listWidget_session.addItem(new_item)
        self.listWidget_session.setCurrentItem(new_item)

    def on_delete_button_clicked(self):
        del_item = self.listWidget_session.takeItem(self.listWidget_session.currentRow())
        del del_item

    def on_session_name_editing_finished(self):
        self.listWidget_session.currentItem().setText(self.lineEdit_name.text())

    def on_setting_button_clicked(self):
        self.settings_dialog = SettingDialog()
        self.settings_dialog.show()

    def on_about_button_clicked(self):
        self.about_dialog = AboutDialog()
        self.about_dialog.exec()

    def on_audio_button_toggled(self, is_clicked):
        if is_clicked:
            self.isSwitchOn = True
            thread = threading.Thread(target=self.start_or_stop_speech_to_text)
            thread.start()
        else:
            self.isSwitchOn = False

    def start_or_stop_speech_to_text(self):
        audio = pyaudio.PyAudio()
        t = SpeechRecognition('user')
        t.start()
        # 开始录音
        stream = audio.open(format=self.for_mat, channels=self.channels,
                            rate=self.rate, input=True,
                            frames_per_buffer=self.chunk)
        print("录音中...")
        while self.isSwitchOn:
            data = stream.read(self.chunk)
            t.send_audio_data(data)  # 发送音频数据片段
            time.sleep(0.01)
            if t.speech_text_end != "":
                self.plainTextEdit_input.insertPlainText(t.speech_text_end)
                t.speech_text_end = ""
            # self.plainTextEdit_input.appendPlainText(t.speech_text_chg)
        print("录音结束")
        t.sr.stop()
        self.plainTextEdit_input.insertPlainText(t.speech_text_end)
        # 停止录音
        stream.stop_stream()
        stream.close()
        audio.terminate()
