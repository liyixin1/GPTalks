import json

import threading

import requests

import config
from groq import Groq


class AIModel:
    def __init__(self):
        self.thread = threading.Thread(target=self.set_ai_parameter)
        self.thread.start()
        self.ai = config.aimodel.ai
        self.api_key = config.aimodel.api_key
        self.model = config.aimodel.model
        self.chat_rounds = config.aimodel.chat_rounds
        self.max_tokens = config.aimodel.max_tokens
        self.chat_prompt = config.aimodel.chat_prompt

        self.openai_url = "https://api.openai.com/v1/chat/completions"
        self.openai_headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.api_key,
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json'
        }
        self.grop_client = Groq(api_key=self.api_key)

    def set_ai_parameter(self):
        while True:
            config.event1.wait()
            self.ai = config.aimodel.ai
            self.api_key = config.aimodel.api_key
            self.openai_headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + self.api_key,
                'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                'Content-Type': 'application/json'
            }
            self.grop_client = Groq(api_key=self.api_key)
            self.model = config.aimodel.model
            self.chat_rounds = config.aimodel.chat_rounds
            self.max_tokens = config.aimodel.max_tokens
            self.chat_prompt = config.aimodel.chat_prompt
            # print("set_gpt_parameter yes")

    # def ai_switch(self, ai):
    #     match ai:
    #         case "OpenAI":
    #             self.url = "https://api.openai.com/v1/chat/completions"
    #             self.headers = {
    #                 'Accept': 'application/json',
    #                 'Authorization': 'Bearer ' + self.api_key,
    #                 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    #                 'Content-Type': 'application/json'
    #             }
    #         case "Grop":
    #             self.client = Groq(api_key=self.api_key)

    def start(self, model, record):
        match model:
            case "OpenAI":
                return self.chat_gpt(record)
            case "Groq":
                return self.groq(record)

    def limit_to_chat_rounds(self, record) -> list:
        if (len(record)) > self.chat_rounds * 2:
            return record[(len(record)) - self.chat_rounds * 2 + 2:]  # 绕开chatGPT内容中的system内容
        else:
            return record

    # GPT模式
    def chat_gpt(self, record) -> list:
        payload = json.dumps({
            "model": self.model,
            "messages": self.limit_to_chat_rounds(record),
            "max_tokens": self.max_tokens
        })

        # print("payload")
        # print(payload)
        response = requests.request("POST", self.openai_url, headers=self.openai_headers, data=payload)
        response_json = response.json()
        # 从响应中获取并返回所需的文本
        print(response_json)
        return response_json.get("choices", [{}])[0].get("message", [])

    # Llama模式
    def groq(self, record) -> dict[str, str]:
        chat_completion = self.grop_client.chat.completions.create(
            messages=record,
            model=self.model,
            temperature=0.5,
            max_tokens=self.max_tokens,
            top_p=1,
            stop=None,
            stream=False,
        )
        response = {'role': 'assistant', 'content': chat_completion.choices[0].message.content}
        return response

    def user_input_to_record_item(self, user_input):
        return {"role": "user", "content": user_input}


aimodel = AIModel()
