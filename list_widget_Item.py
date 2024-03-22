from PyQt6 import QtWidgets

from chatgpt import chatgpt

from chat_record import chat_record_log


class ListWidgetItem(QtWidgets.QListWidgetItem):

    def __init__(self, name: str):
        super().__init__(name)
        self.record = [
            {
                "role": "system",
                "content": chatgpt.chat_prompt
            }
        ]

    def get_record(self, user_input, item_name) -> str:
        if user_input:
            self.record.append(chatgpt.user_input_to_record_item(user_input))
            chat_record_log.save_record_to_log(self.record[-1], item_name)
            chatgpt_reply = chatgpt.get_gpt_response(self.record)
            self.record.append(chatgpt_reply)
            chat_record_log.save_record_to_log(self.record[-1], item_name)
        return self.record_to_display_text()

    def record_to_display_text(self) -> str:
        return_record = []
        for i in self.record:
            if i['role'] == "user":
                return_record.append("你：" + i['content'])
            elif i['role'] == "assistant":
                return_record.append("chatGPT:" + i['content'])
        return '\n'.join(return_record)
