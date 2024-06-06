"""
list_widget_item.py
处理聊天记录并与用户互动。
"""
from tkinter import messagebox
import markdown
from PyQt6 import QtWidgets
from ai_model import aimodel
from chat_record import chat_record_log


class ListWidgetItem(QtWidgets.QListWidgetItem):
    """管理聊天项目的类，存储聊天记录并处理用户输入。"""
    def __init__(self, name: str):
        super().__init__(name)
        self.record = [
            {
                "role": "system",
                "content": aimodel.config["chat_prompt"]
            }
        ]

    def get_record(self, user_input, item_name) -> str:
        """处理用户输入，调用AI模型生成回复，并将聊天记录保存及展示。"""
        if not user_input:
            return self.record_to_display_text()

        # 将用户输入保存到记录中
        self.record.append(aimodel.user_input_to_record_item(user_input))
        chat_record_log.save_record_to_log(self.record[-1], item_name)
        chat_record_log.chat_debug(self.record)

        # 尝试生成AI回复
        try:
            chatgpt_reply = aimodel.start(aimodel.config["ai"], self.record)
            print(chatgpt_reply)
            # 检查回复中是否有错误信息
            if 'error' in chatgpt_reply:
                raise ValueError(f"API Error: {chatgpt_reply['error']['message']}")
            # 保存AI回复至记录中
            self.record.append(chatgpt_reply)
            chat_record_log.save_record_to_log(self.record[-1], item_name)
            return self.record_to_display_text()
        except TypeError as e:
            messagebox.showwarning("警告", f"出现错误，请检查配置: {str(e)}")
            # 恢复记录状态
            self.record.pop()
            self.record.pop()
            return self.record_to_display_text()

    def record_to_display_text(self) -> str:
        """将聊天记录转换为Markdown格式的HTML文本以供展示。"""
        return_record = []
        for i in self.record:
            if i['role'] == "user":
                return_record.append("### 你：\n" + i['content'])
            elif i['role'] == "assistant":
                return_record.append("### Assistant:\n" + i['content'])
            # elif i['role'] == "Groq":
            #     return_record.append("### Groq:\n" + i['content'])

        html_text = markdown.markdown('\n'.join(return_record),
                                      extensions=[
                                          'abbr',
                                          'attr_list',
                                          'def_list',
                                          'fenced_code',
                                          'footnotes',
                                          'tables',
                                      ])
        return html_text
