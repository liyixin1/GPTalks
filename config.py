"""
config.py
配置各种接口Key以及其他参数。
"""
import threading
import tomli
import tomlkit


def read_toml_file(file_path):
    """读取配置文件"""
    with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
        toml_dict = tomli.load(f)
    return toml_dict


event1 = threading.Event()


class AiModel:
    """配置模型参数"""
    def __init__(self):
        self.thread = threading.Thread(target=self.write_to_config)
        self.thread.start()
        self.api_key = read_toml_file("config.toml")["ai_model"]["api_key"]
        self.ai = read_toml_file("config.toml")["ai_model"]["ai"]
        self.model = read_toml_file("config.toml")["ai_model"]["model"]
        self.chat_rounds = read_toml_file("config.toml")["ai_model"]["chat_rounds"]
        self.max_tokens = read_toml_file("config.toml")["ai_model"]["max_tokens"]
        self.chat_prompt = read_toml_file("config.toml")["ai_model"]["chat_prompt"]

    def write_to_config(self):
        """当识别到用户通过GUI修改参数时，自动同步写入配置文件config.toml"""
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


