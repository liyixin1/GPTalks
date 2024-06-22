"""对话记录模块"""
import os
from datetime import datetime


class ChatRecordMd:
    """聊天记录存储"""

    def __init__(self):
        self.today = datetime.now().date()
        self.dir = './chat_record_mds/' + str(self.today)
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def save_record_to_md(self, record, item_name):
        """将对话记录保存到日志文件"""
        md_file = str(datetime.now().date()) + '_' + item_name + '.md'
        log_file_path = os.path.join(self.dir, md_file)
        with open(log_file_path, 'a', encoding='utf-8') as f:
            if record['role'] == 'user':
                data = ""
                for content_item in record['content']:
                    if 'text' in content_item:
                        data += content_item['text'] + "\n"
                    elif 'image_url' in content_item:
                        image_data_base64 = content_item['image_url']['url']
                        image_data_html = f'<img src="{image_data_base64}"/>\n'
                        data += image_data_html
                self.write_to_markdown_with_timestamp('user', f, data)
            elif record['role'] == 'assistant':
                text = record['content']
                self.write_to_markdown_with_timestamp('assistant', f, text)

    def write_to_markdown_with_timestamp(self, role, file, content):
        """写入文件"""
        # 获取当前时间并格式化为字符串
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 构建Markdown格式的时间戳和内容
        markdown_content = f"\n## {current_time}-{role}\n{content}\n"

        file.write(markdown_content)


chat_record_md = ChatRecordMd()
