"""
config.py
配置各种接口Key以及其他参数。
"""
import threading
import tomlkit


def read_toml_file(file_path):
    """读取配置文件"""
    with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
        toml_dict = tomlkit.load(f)
    return toml_dict


event1 = threading.Event()


class ConfigManager:
    """配置模型参数"""
    def __init__(self):
        self.thread = threading.Thread(target=self.write_to_config)
        self.thread.start()
        self.ai_parameter = {
            "api_key": self.read_toml_file("config.toml")["ai_model"]["api_key"],
            "ai": self.read_toml_file("config.toml")["ai_model"]["ai"],
            "model": self.read_toml_file("config.toml")["ai_model"]["model"],
            "chat_rounds": self.read_toml_file("config.toml")["ai_model"]["chat_rounds"],
            "max_tokens": self.read_toml_file("config.toml")["ai_model"]["max_tokens"],
            "chat_prompt": self.read_toml_file("config.toml")["ai_model"]["chat_prompt"]
        }
        self.display = {
            'language': self.read_toml_file('config.toml')["display"]["language"],
            'theme': self.read_toml_file('config.toml')["display"]["theme"],
            'font_size': self.read_toml_file('config.toml')["display"]["font_size"],
        }

    def read_toml_file(self, file_path):
        """读取配置文件"""
        with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
            toml_dict = tomlkit.load(f)
        return toml_dict

    def write_to_config(self):
        """当识别到用户通过GUI修改参数时，自动同步写入配置文件config.toml"""
        while True:
            event1.wait()
            with open('config.toml', 'r', encoding='utf-8') as f:
                data = tomlkit.parse(f.read())
            data['ai_model']['ai'] = self.ai_parameter['ai']
            data['ai_model']['api_key'] = self.ai_parameter['api_key']
            data['ai_model']['model'] = self.ai_parameter['model']
            data['ai_model']['max_tokens'] = int(self.ai_parameter['max_tokens'])
            data['ai_model']['chat_rounds'] = int(self.ai_parameter['chat_rounds'])
            data['ai_model']['chat_prompt'] = self.ai_parameter['chat_prompt']

            data['display']['language'] = self.display['language']
            data['display']['theme'] = self.display['theme']
            data['display']['font_size'] = self.display['font_size']
            # 将修改后的数据写回文件
            with open('config.toml', 'w', encoding='utf-8') as f:
                f.write(tomlkit.dumps(data))
            print("write_to_config yes")


configmanager = ConfigManager()
