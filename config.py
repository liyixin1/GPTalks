import os

import tomli
import tomlkit


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
        self.model = read_toml_file("config.toml")["openai"]["model"]
        self.chat_rounds = read_toml_file("config.toml")["openai"]["chat_rounds"]
        self.max_tokens = read_toml_file("config.toml")["openai"]["max_tokens"]
        self.chat_prompt = read_toml_file("config.toml")["openai"]["chat_prompt"]

    def get_gpt_parameter(self, api_key, model, max_tokens, chat_rounds, chat_prompt):
        self.api_key = api_key
        self.model = model
        self.chat_rounds = int(chat_rounds)
        self.max_tokens = int(max_tokens)
        self.chat_prompt = chat_prompt

    def write_to_config(self, model, max_tokens, chat_rounds, chat_prompt):
        with open('config.toml', 'r', encoding='utf-8') as f:
            data = tomlkit.parse(f.read())
        data['openai']['model'] = model
        data['openai']['max_tokens'] = int(max_tokens)
        data['openai']['chat_rounds'] = int(chat_rounds)
        data['openai']['chat_prompt'] = chat_prompt
        # 将修改后的数据写回文件
        with open('config.toml', 'w', encoding='utf-8') as f:
            f.write(tomlkit.dumps(data))


openai = Openai()
