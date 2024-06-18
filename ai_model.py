"""此模块提供多种AI交互"""
import json
import threading
import requests
import config


class AIModel:
    """封装了GPT模型、Llama模型交互的逻辑，处理与模型的通信"""

    def __init__(self):
        thread = threading.Thread(target=self.set_ai_parameter)
        thread.start()
        self.config = {
            "ai": config.aimodel.ai,
            "api_key": config.aimodel.api_key,
            "model": config.aimodel.model,
            "chat_rounds": config.aimodel.chat_rounds,
            "max_tokens": config.aimodel.max_tokens,
            "chat_prompt": config.aimodel.chat_prompt,
        }

        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.config["api_key"],
            'Content-Type': 'application/json'
        }
        self.url = {
            'OpenAI': "https://api.openai.com/v1/chat/completions",
            'Groq': "https://api.groq.com/openai/v1/chat/completions",
        }

    def set_ai_parameter(self):
        """线程无限等待，直到检测到用户更改设置信号的出现"""
        while True:
            config.event1.wait()
            self.config["ai"] = config.aimodel.ai
            self.config["api_key"] = config.aimodel.api_key
            self.headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + self.config["api_key"],
                'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                'Content-Type': 'application/json'
            }
            self.config["model"] = config.aimodel.model
            self.config["chat_rounds"] = config.aimodel.chat_rounds
            self.config["max_tokens"] = config.aimodel.max_tokens
            self.config["chat_prompt"] = config.aimodel.chat_prompt

    def start(self, record):
        """入口函数"""
        try:
            # 获取AI响应
            return self.get_ai_response(self.config["ai"], record)
        except requests.exceptions.RequestException as e:
            # 处理网络请求异常，如连接错误、超时等
            print(f"Network request failed: {e}")
            return None
        except (ValueError, TypeError) as e:
            # 处理可能的JSON解析错误或其他值错误
            print(f"JSON parsing or type error occurred: {e}")
            return None

    def get_ai_response(self, model, record):
        """通过POST请求向指定的AI模型发送数据，并接收响应"""
        payload = json.dumps({
            "model": self.config["model"],
            "messages": self.limit_to_chat_rounds(record),
            "max_tokens": self.config["max_tokens"]
        })
        response = requests.request("POST",
                                    self.url[model],
                                    headers=self.headers,
                                    data=payload,
                                    timeout=100,
                                    )
        response_json = response.json()
        return response_json["choices"][0].get("message", [])

    def limit_to_chat_rounds(self, record) -> list:
        """多轮对话控制器，当超出用户设置的回合数后即触发丢弃一回合对话内容，先进先出。"""
        if (len(record)) > self.config["chat_rounds"] * 2:
            # +2绕开内容中的system内容
            return record[(len(record)) - self.config["chat_rounds"] * 2 + 2:]
        return record

    def user_input_image_to_record_item(self, user_input, user_image=None):
        """处理用户输入的文字和可能存在的图片"""
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input
                    }
                ]
            }
        ]
        if user_image:
            messages[0]["content"].append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{user_image}"
                }
            })
        return messages[0]


aimodel = AIModel()
