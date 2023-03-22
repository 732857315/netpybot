
import requests

api_key = "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"
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(api_key)
}
msg="请用C语言写一个霍夫曼编码。"
params ={
    "model": "gpt-3.5-turbo-0301",
    "messages":[
        {"role":"user","content":"{0}".format(msg)}   
    ]
}
print("测试问题："+msg)
try:
    response = requests.post(url, headers=headers, json=params)
    try:
        print(response.json()["choices"][0]["message"]["content"])
    except:
        print(response.json())
except:
    print("连接openai出错.")
