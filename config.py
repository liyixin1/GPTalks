import os
import sys
import threading

import tomli
import tomlkit
import mysql.connector


def read_toml_file(file_path):
    with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
        toml_dict = tomli.load(f)
    return toml_dict


event1 = threading.Event()


class AiModel:
    def __init__(self):
        self.thread = threading.Thread(target=self.write_to_config)
        self.thread.start()
        if not read_toml_file("config.toml")["ai_model"]["api_key"]:
            self.api_key = os.getenv("OPENAI_API_KEY")
        else:
            self.api_key = read_toml_file("config.toml")["ai_model"]["api_key"]
        self.ai = read_toml_file("config.toml")["ai_model"]["ai"]
        self.model = read_toml_file("config.toml")["ai_model"]["model"]
        self.chat_rounds = read_toml_file("config.toml")["ai_model"]["chat_rounds"]
        self.max_tokens = read_toml_file("config.toml")["ai_model"]["max_tokens"]
        self.chat_prompt = read_toml_file("config.toml")["ai_model"]["chat_prompt"]

    def write_to_config(self):
        while True:
            event1.wait()
            with open('config.toml', 'r', encoding='utf-8') as f:
                data = tomlkit.parse(f.read())
            data['ai_model']['ai'] = self.ai
            data['ai_model']['api_key'] = self.api_key
            data['ai_model']['model'] = self.model
            data['ai_model']['max_tokens'] = int(self.max_tokens)
            data['ai_model']['chat_rounds'] = int(self.chat_rounds)
            data['ai_model']['chat_prompt'] = self.chat_prompt
            # 将修改后的数据写回文件
            with open('config.toml', 'w', encoding='utf-8') as f:
                f.write(tomlkit.dumps(data))
            print("write_to_config yes")


aimodel = AiModel()


class Aliyun:
    def __init__(self):
        if not read_toml_file("config.toml")["aliyun"]["access_key_id"]:
            self.access_key_id = os.getenv("ALIYUN_AK_ID")
        else:
            self.access_key_id = read_toml_file("config.toml")["aliyun"]["access_key_id"]

        if not read_toml_file("config.toml")["aliyun"]["access_key_secret"]:
            self.access_key_secret = os.getenv("ALIYUN_AK_SECRET")
        else:
            self.access_key_secret = read_toml_file("config.toml")["aliyun"]["access_key_secret"]
        self.app_key = read_toml_file("config.toml")["aliyun"]["app_key"]


aliyun = Aliyun()


class DateBase:
    def __init__(self):
        # 数据库连接配置
        self.db_config = {
            'user': 'root',
            'password': '88888888',
            'host': 'localhost',
            'database': 'gpt_data'
        }

    def get_connection(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            # print("数据库连接成功。")
            return conn
        except mysql.connector.Error as e:
            print("数据库连接失败:", e)
            # 在这里处理连接失败的情况

    def close_connection(self, conn, cursor):
        if conn is not None:
            cursor.close()
            conn.close()


database = DateBase()
