import os

import requests
import json

import config


class ChatGPT:
    def __init__(self):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.api_key = config.openai.api_key
        self.model = config.openai.model
        self.chat_rounds = config.openai.chat_rounds
        self.max_tokens = config.openai.max_tokens
        self.chat_prompt = config.openai.chat_prompt
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.api_key,
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json'
        }

    def user_input_to_record_item(self, user_input):
        return {"role": "user", "content": user_input}

    def limit_to_chat_rounds(self, record) -> list:
        if (len(record)) > self.chat_rounds * 2:
            return record[(len(record)) - self.chat_rounds * 2 + 2:]  # 绕开发给chatGPT内容中的system内容
        else:
            return record

    def get_gpt_response(self, record) -> list:
        # messages = [
        #     {
        #         "role": "user",
        #         "content": user_input
        #     }
        # ]
        payload = json.dumps({
            "model": self.model,
            "messages": self.limit_to_chat_rounds(record),
            "max_tokens": self.max_tokens
        })

        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        response_json = response.json()
        # 从响应中获取并返回所需的文本
        return response_json.get("choices", [{}])[0].get("message", [])

    def set_gpt_parameter(self):
        if not config.openai.api_key:
            self.api_key = os.getenv("OPENAI_API_KEY")
        else:
            self.api_key = config.openai.api_key
        self.model = config.openai.model
        self.chat_rounds = config.openai.chat_rounds
        self.max_tokens = config.openai.max_tokens
        self.chat_prompt = config.openai.chat_prompt


chatgpt = ChatGPT()
