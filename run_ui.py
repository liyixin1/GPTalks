from PyQt6.QtWidgets import QApplication, QMainWindow
from main_window_ui import Ui_MainWindow  # 从你的 UI 文件中导入 UI 类

import sys


def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
