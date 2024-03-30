import os
import threading

import tomli
import tomlkit


def read_toml_file(file_path):
    with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
        toml_dict = tomli.load(f)
    return toml_dict


event = threading.Event()


class Openai:
    def __init__(self):
        self.thread = threading.Thread(target=self.write_to_config)
        self.thread.start()
        if not read_toml_file("config.toml")["openai"]["api_key"]:
            self.api_key = os.getenv("OPENAI_API_KEY")
        else:
            self.api_key = read_toml_file("config.toml")["openai"]["api_key"]
        self.model = read_toml_file("config.toml")["openai"]["model"]
        self.chat_rounds = read_toml_file("config.toml")["openai"]["chat_rounds"]
        self.max_tokens = read_toml_file("config.toml")["openai"]["max_tokens"]
        self.chat_prompt = read_toml_file("config.toml")["openai"]["chat_prompt"]

    def write_to_config(self):
        while True:
            event.wait()
            print(self.chat_rounds)
            with open('config.toml', 'r', encoding='utf-8') as f:
                data = tomlkit.parse(f.read())
            data['openai']['model'] = self.model
            data['openai']['max_tokens'] = int(self.max_tokens)
            data['openai']['chat_rounds'] = int(self.chat_rounds)
            data['openai']['chat_prompt'] = self.chat_prompt
            # 将修改后的数据写回文件
            with open('config.toml', 'w', encoding='utf-8') as f:
                f.write(tomlkit.dumps(data))
            print("write_to_config yes")


openai = Openai()


class Aliyun(object):
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
