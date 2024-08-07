"""
main.py
程序入口
"""
import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """创建主窗口实例"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return_value = app.exec()  # 监听事件直到窗体退出
    sys.exit(return_value)  # 回收资源并向系统返回值


if __name__ == '__main__':
    main()
