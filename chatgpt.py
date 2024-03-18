import requests
import json

import tomli

url = "https://api.openai.com/v1/chat/completions"


def read_toml_file(file_path):
    with open(file_path, "rb") as f:  # TOML文件需要以二进制模式打开
        toml_dict = tomli.load(f)
    return toml_dict


config = read_toml_file("config.toml")
open_key = config["openai"]["api_key"]


def get_gpt_response(user_input):
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    # 从响应中获取并返回所需的文本
    return response_json.get("choices", [{}])[0].get("message", {}).get("content", "")


headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + open_key,
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}
