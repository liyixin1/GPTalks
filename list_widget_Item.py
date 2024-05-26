from tkinter import messagebox

import markdown
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget

from ai_model import aimodel

from chat_record import chat_record_log


class ListWidgetItem(QtWidgets.QListWidgetItem):

    def __init__(self, name: str):
        super().__init__(name)
        self.record = [
            {
                "role": "system",
                "content": aimodel.chat_prompt
            }
        ]

    def get_record(self, user_input, item_name) -> str:
        if user_input:
            self.record.append(aimodel.user_input_to_record_item(user_input))
            chat_record_log.save_record_to_log(self.record[-1], item_name)
            chat_record_log.chat_debug(self.record)
            try:
                chatgpt_reply = aimodel.start(aimodel.ai, self.record)
                print(chatgpt_reply)
                if 'error' in chatgpt_reply:
                    raise ValueError(f"API Error: {chatgpt_reply['error']['message']}")
                else:
                    self.record.append(chatgpt_reply)
                    chat_record_log.save_record_to_log(self.record[-1], item_name)
                    return self.record_to_display_text()
            except Exception as e:
                messagebox.showwarning("警告", "请检查配置")
                self.record.pop()
                self.record.pop()
                return self.record_to_display_text()

    def record_to_display_text(self) -> str:
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
