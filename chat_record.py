"""对话记录模块"""
import base64
import logging
import os
from datetime import datetime


class ChatRecordLog:
    """聊天记录存储"""
    def __init__(self):
        self.today = datetime.now().date()
        self.log_dir = './chat_record_logs/' + str(self.today)
        self.image_dir = './chat_record_logs/' + str(self.today) + "-img"
        self.user_log = logging.getLogger("user")
        self.reply_log = logging.getLogger('assistant')
        self.debug_log = logging.getLogger('debug')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)

    def save_record_to_log(self, record, item_name):
        """将对话记录保存到日志文件"""
        log_file = str(datetime.now().date()) + '_' + item_name + '.log'
        log_file_path = os.path.join(self.log_dir, log_file)
        logging.basicConfig(filename=log_file_path,
                            filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%a %d %b %Y %H:%M:%S',
                            level=logging.INFO,
                            encoding='utf-8')
        if record['role'] == 'user':
            for content_item in record['content']:
                if 'text' in content_item:
                    text = content_item['text'] + "\n"
                    self.user_log.info(text)
                elif 'image_url' in content_item:
                    try:
                        image_data = content_item['image_url']['url']
                        # 使用split方法分割字符串
                        parts = image_data.split("data:image/jpeg;base64,", 1)
                        if len(parts) > 1:
                            image_data = parts[1]
                        else:
                            image_data = parts[0]
                        image_path = os.path.join(self.image_dir,
                                                  f"{datetime.now().strftime('%Y%m%d%H%M%S')}.jpeg")
                        with open(image_path, 'wb') as f:
                            f.write(base64.b64decode(image_data))
                        self.user_log.info(image_path)
                    except IOError as e:
                        logging.error(e)
        elif record['role'] == 'assistant':
            self.reply_log.info(record['content'])

    def chat_debug(self, record):
        """记录错误警告"""
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.debug_log.debug(record)


chat_record_log = ChatRecordLog()
