"""
list_widget_item.py
处理聊天记录并与用户互动。
"""
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

    def get_record(self, user_input, user_image, item_name) -> str:
        """处理用户输入，调用AI模型生成回复，并将聊天记录保存及展示。"""
        if not user_input:
            return self.record_to_display_text()

        # 将用户输入保存到记录中
        self.record.append(aimodel.user_input_image_to_record_item(user_input, user_image))
        chat_record_log.save_record_to_log(self.record[-1], item_name)
        chat_record_log.chat_debug(self.record)

        # 尝试生成AI回复
        chat_reply = aimodel.start(self.record)
        # 检查回复中是否有错误信息
        if 'Error' in chat_reply:
            self.record.pop()
            return chat_reply
        # 保存AI回复至记录中
        self.record.append(chat_reply)
        chat_record_log.save_record_to_log(self.record[-1], item_name)
        return self.record_to_display_text()


    def record_to_display_text(self) -> str:
        """将聊天记录转换为Markdown格式的HTML文本显示。"""
        return_record = []
        for i in self.record:
            if i['role'] == "user":
                try:
                    # 提取文本内容
                    text_content = i['content'][0]['text'] + "\n"
                    # 处理图片
                    image_urls = [content['image_url']["url"]
                                  for content in i['content'] if content.get('type') == "image_url"
                                  and 'image_url' in content]
                    for image_url in image_urls:
                        text_content += (f'\n<img src="{image_url}"'
                                         f'width="300" style="height:auto;">')
                    return_record.append("### 你：\n" + text_content)
                except (KeyError, IndexError, TypeError) as e:
                    # 报错
                    return_record.append(f"### 你：\nError processing content: {e}")
            elif i['role'] == "assistant":
                try:
                    return_record.append("### Assistant:\n" + i['content'])
                except KeyError as e:
                    # 报错
                    return_record.append(f"### Assistant:\nError processing content: {e}")

        html_text = markdown.markdown('\n'.join(return_record),
                                      extensions=[
                                          'abbr',
                                          'attr_list',
                                          'def_list',
                                          'fenced_code',
                                          'footnotes',
                                          'tables',
                                      ]
                                      )
        return html_text

    def get_current_model(self):
        """主窗口调用，返回当前的model"""
        return aimodel.config["model"]
