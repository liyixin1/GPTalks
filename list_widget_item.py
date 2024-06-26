"""
list_widget_item.py
处理聊天记录并与用户互动。
"""
import markdown
from PyQt6 import QtWidgets
from ai_model import aimodel
from chat_record import chat_record_md


class ListWidgetItem(QtWidgets.QListWidgetItem):
    """管理聊天项目的类，存储聊天记录并处理用户输入。"""

    def __init__(self, name: str):
        super().__init__(name)
        self.record = [
            {
                "role": "system",
                "content": aimodel.ai_parameter["chat_prompt"] + "确保你回答的内容格式是markdown。"
            }
        ]

    def get_record(self, user_input, user_image, item_name) -> dict:
        """处理用户输入，调用AI模型生成回复，并将聊天记录保存及展示。"""
        # 将用户输入保存到记录中
        self.record.append(aimodel.user_input_image_to_record_item(user_input, user_image))
        chat_record_md.save_record_to_md(self.record[-1], item_name)

        # 尝试生成AI回复
        chat_reply = aimodel.start(self.record)
        # 检查回复中是否有错误信息
        if chat_reply.get('Error') is not None:
            self.record.pop()
            return chat_reply
        # 保存AI回复至记录中
        self.record.append(chat_reply.get('OK'))
        chat_record_md.save_record_to_md(self.record[-1], item_name)
        return {'OK': self.record_to_display_text()}

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
        # print(html_text)
        self.set_code_styles(html_text)
        return self.set_code_styles(html_text)

    def get_current_model(self):
        """主窗口调用，返回当前的model"""
        return aimodel.ai_parameter["model"]

    def set_code_styles(self, html_text):
        html_with_styles = f"""
                <html>
                <head>
                    <style type="text/css">
                        pre {{
                                background-color: #2b2b2b; /* 深色背景 */
                                color: #f8f8f2; /* 浅色文本 */
                                font-family: 'Consolas', 'Courier New', Courier, monospace; /* 等宽字体 */
                                padding: 15px; /* 增加内边距 */
                                border-radius: 5px; /* 圆角 */
                                border: 1px solid #ccc; /* 边框 */
                                line-height: normal; /* 行间距 */
                                overflow: auto; /* 显示滚动条 */
                        }}
                        code {{
                                background-color: #2b2b2b; /* 深色背景 */
                                color: #f8f8f2; /* 浅色文本 */
                                font-family: 'Consolas', 'Courier New', Courier, monospace; /* 等宽字体 */
                                padding: 0; /* 去除内边距 */
                                margin: 0; /* 去除外边距 */
                                line-height: normal; /* 行间距 */
                        }}
                    </style>
                </head>
                <body>
                    {html_text}
                </body>
                </html>
                """
        return html_with_styles
