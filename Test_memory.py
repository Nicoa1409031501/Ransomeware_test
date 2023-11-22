

import requests
import json

API_KEY = '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'
Role_Set = "You are a helpful assistant."

def post_prompt(messages):
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-3.5-turbo-0613',
            'messages': messages
        }
    )
    
    return response.json()

# 初始化对话历史
conversation_history = [
    {"role": "system", "content": Role_Set}
]

# 模拟对话流程
user_inputs = ["Hello, who are you?", "Can you tell me about machine learning?","早安","午安"]

for user_input in user_inputs:
    # 添加用户的新输入
    conversation_history.append({"role": "user", "content": user_input})

    # 发送请求并获取回答
    response = post_prompt(conversation_history)
    assistant_response = response['choices'][0]['message']['content']
    print("Assistant:", assistant_response)

    # 添加助手的回答到对话历史
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
with open("./Response_from_ChatGPT/123123123.json","w+",encoding="utf8") as file_json:

    json.dump(response.json(),file_json,indent=2, separators=(',', ':'),ensure_ascii=False)