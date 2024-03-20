import os

import tomli


def read_toml_file(file_path):
    with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
        toml_dict = tomli.load(f)
    return toml_dict


class Openai:
    def __init__(self):
        if not read_toml_file("config.toml")["openai"]["api_key"]:
            self.api_key = os.getenv("OPENAI_API_KEY")
        else:
            self.api_key = read_toml_file("config.toml")["openai"]["api_key"]
        self.chat_rounds = read_toml_file("config.toml")["openai"]["chat_rounds"]
        self.model = read_toml_file("config.toml")["openai"]["model"]
        self.max_tokens = read_toml_file("config.toml")["openai"]["max_tokens"]


openai = Openai()
