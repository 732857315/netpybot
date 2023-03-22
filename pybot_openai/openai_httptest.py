import json
import requests

URL = "https://api.openai.com/v1/completions"
api_key = "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"
##class ChatGPT(object):
##    @staticmethod
##    def GetApi(prompt, authorization, model="text-davinci-003", temperature=0, max_tokens=3000):
##        data = json.dumps({
##            "model": model,
##            "prompt": prompt,
##            "temperature": temperature,
##            "max_tokens": max_tokens
##            # "stream": True
##        })
##        headers = {
##            "Content-Type": "application/json",
##            "Authorization": "Bearer {}".format(authorization)
##        }
##        response = requests.post(url=URL, headers=headers, data=data)
##        result = response.json()
##        return (result or {}).get("choices", [])
data = json.dumps({
    "model": "text-davinci-003",
    "prompt": "写一个C语言hellowold示例",
    "temperature": 0,
    "max_tokens": 3000
    # "stream": True
})
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(api_key)
}
#try:
response = requests.post(url=URL, headers=headers, data=data,timeout = 500)#(6,9)
##except:
##    response = "ERROR!"
#result = response.json()
print(str(response))
