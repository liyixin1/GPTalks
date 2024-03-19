from PyQt6 import QtWidgets

from chatgpt import get_gpt_response, user_input_to_record_item


class ListWidgetItem(QtWidgets.QListWidgetItem):

    def __init__(self, name: str):
        super().__init__(name)
        self.record = []

    def get_record(self, user_input) -> str:
        return_record = []
        self.record.append(user_input_to_record_item(user_input))
        chatgpt_reply = get_gpt_response(self.record)
        self.record.append(chatgpt_reply)
        print(self.record)
        for i in self.record:
            if i['role'] == "user":
                return_record.append("你：" + i['content'])
            else:
                return_record.append("chatGPT:" + i['content'])

        return '\n'.join(return_record)
