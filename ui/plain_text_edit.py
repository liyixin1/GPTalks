from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QPlainTextEdit


class MyPlainTextEdit(QPlainTextEdit):
    # 定义一个名为ctrlEnterPressed的信号
    ctrlEnterPressed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        # 检测是否同时按下了Ctrl和Enter键
        if event.key() == Qt.Key.Key_Return and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            self.ctrlEnterPressed.emit()  # 发射信号
        else:
            # 如果不是我们想要捕捉的按键，则调用基类的keyPressEvent来保持正常的按键行为
            super().keyPressEvent(event)
