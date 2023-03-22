
import requests
# Your OpenAI APIKey
api_key = "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"
# The text prompt you want to generate a response
input_prompt = input("输入需要跟chat AI的聊天内容：")
prompt = input_prompt
# The URL for OpenAI'sAPI
url = 'https://api.openai.com/v1/completions'
# The headers for the APIrequest
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
params ={
    "model": "text-davinci-003",
    "prompt": prompt,
    "temperature": 0.7,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
    }
# Make the API
requestresponse = requests.post(url, headers=headers, json=params)# Check if the request wassuccessful
if response.status_code == 200:    # Extract the generated text from the response
    generated_text = response.json()["choices"][0]["text"]
    print(generated_text)
else:    # Handle the error
    print(f"Request failed with status code {response.status_code}")
#url，需要请求的API地址
#headers：    "Content-Type": "application/json","Authorization": f"Bearer {api_key}"
#请求头json：需要传递的参数，其参数跟使用openai库类似，需要提供模型名称，prompt以及其他基础参数等
