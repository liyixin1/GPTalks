import requests
import json

import config

url = "https://api.openai.com/v1/chat/completions"

open_key = config.openai.api_key


def user_input_to_record_item(user_input):
    return {"role": "user", "content": user_input}


def get_gpt_response(record) -> list:
    # messages = [
    #     {
    #         "role": "user",
    #         "content": user_input
    #     }
    # ]
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": record
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    # 从响应中获取并返回所需的文本
    return response_json.get("choices", [{}])[0].get("message", [])


headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + open_key,
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}
