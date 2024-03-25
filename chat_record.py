import logging
import os
from datetime import datetime


class ChatRecordLog:
    def __init__(self):
        self.today = datetime.now().date()
        if not os.path.exists('./chat_record_logs'):
            os.makedirs('./chat_record_logs')
        self.log_dir = './chat_record_logs/' + str(self.today)
        self.user_log = logging.getLogger("user")
        self.chatgpt_log = logging.getLogger('chatgpt')
        self.debug_log = logging.getLogger('debug')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def save_record_to_log(self, record, item_name):
        log_file = str(datetime.now().date()) + '_' + item_name + '.log'
        log_file_path = os.path.join(self.log_dir, log_file)
        logging.basicConfig(filename=log_file_path,
                            filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%a %d %b %Y %H:%M:%S',
                            level=logging.INFO,
                            encoding='utf-8')
        if record['role'] == 'user':
            self.user_log.info(record['content'])
        elif record['role'] == 'assistant':
            self.chatgpt_log.info(record['content'])

    def chat_debug(self, record):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.debug_log.debug(record)


chat_record_log = ChatRecordLog()
