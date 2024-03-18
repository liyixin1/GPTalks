import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from main_window_ui import Ui_MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()  # 显示窗体
    return_value = app.exec()  # 监听事件直到窗体退出
    sys.exit(return_value)  # 回收资源并向系统返回值


if __name__ == '__main__':
    main()
