#import openai
import requests
import platform
import operator
import importlib
import sys,os

currentDir = os.getcwd()
os.chdir('../pybot_openai/') # .. to go back one dir | you can do "../aFolderYouWant"
sys.path.insert(0, os.getcwd())

systemname = platform.platform()
systembits = platform.architecture()
if (operator.eq(('64bit', 'WindowsPE'),systembits)):
    pyddir="PYD_WIN_AMD64" #pyddir="PYD_WIN_X86"
elif (('64bit', 'ELF') == systembits ):
    pyddir="PYD_LINUX"
else: #苹果('64bit', '')
    pyddir="PYD_OTHERS"
#print(systembits)
#print(pyddir)

pybot_openai_key = importlib.import_module(pyddir+".pybot_openai_key")

os.chdir(currentDir) # to go back to your home directory

#openai.api_key = pybot_openai_key.apikey(1)

##def api_openai_chatgpt3(msg):
##    #msg=input()
##    try:
##        response = openai.Completion.create(
##            engine="text-davinci-003", # text-davinci-003 gpt-3.5-turbo-0301
##            prompt=msg,# 用户提供的输入文本，用于指导GPT输出
##            temperature=0.9,# 控制输出的多样性，0-1，其中0表示最保守的输出，1表示最多样化的输出。
##            # 输出的最大长度（输入+输出的token不能大于模型的最大token）,可以动态调整
##            max_tokens=3500,
##            # [控制字符的重复度] -2.0 ~ 2.0 之间的数字，正值会根据新 tokens 在文本中的现有频率对其进行惩罚，从而降低模型逐字重复同一行的可能性
##            #frequency_penalty=0.2,
##            # [控制主题的重复度] -2.0 ~ 2.0 之间的数字，正值会根据到目前为止是否出现在文本中来惩罚新 tokens，从而增加模型谈论新主题的可能性
##            #presence_penalty=0.15,
##        )
##        return response["choices"][0]["text"]
##    except:
##        mess = "连接openai出错."
##        return mess
##def api_openai_chatgpt3turbo(msg):
##    #msg=input()
##    try:
##        response = openai.Completion.create(
##            model="gpt-3.5-turbo-0301", # text-davinci-003 gpt-3.5-turbo-0301
##            messages=[
##                #{"role":"system","content":msg},
##                #{"role":"assistant","content":msg},
##                {"role":"user","content":msg}
##            ]# 用户提供的输入文本，用于指导GPT输出
##        )
##        return response.json()["choices"][0]["message"]["content"]
##    except:
##        mess = "连接openai出错."
##        return mess

api_key = pybot_openai_key.apikey(1)

#msg="请用C语言写一个霍夫曼编码。"
def api_openai_chatgpt3turbo(msg):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(api_key)
    }
    params ={
        "model": "gpt-3.5-turbo-0301",
        "messages":[
            {"role":"user","content":"{0}".format(msg)}   
        ]
    }
    #print("测试问题："+msg)
    try:
        response = requests.post(url, headers=headers, json=params)
        try:
            return (response.json()["choices"][0]["message"]["content"])
        except:
            return (response.json())
    except:
        mess = "连接openai出错."
        return mess
##4.获取credit_grants（信用补贴）
##
##---------GET：
##curl https://api.openai.com/dashboard/billing/credit_grants \
##-H "Content-Type: application/json" \
##-H "Authorization: Bearer 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"
##
##curl https://api.openai.com/dashboard/billing/credit_grants -H "Content-Type: application/json" -H "Authorization: Bearer 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"
##返回：
##{
##  "object": "credit_summary",
##  "total_granted": 18.0,
##  "total_used": 1.1047,
##  "total_available": 16.8953,
##  "grants": {
##    "object": "list",
##    "data": [
##      {
##        "object": "credit_grant",
##        "id": "36767b23-0006-4145-8bb0-4084541f0407",
##        "grant_amount": 18.0,
##        "used_amount": 1.1047,
##        "effective_at": 1675900800.0, #日期：1970年到今天的秒数，时间戳
##        "expires_at": 1685577600.0
##      }
##    ]
##  }
##}
def api_openai_credit_grants():
    url = "https://api.openai.com/dashboard/billing/credit_grants"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(api_key)
    }
    try:
        response = requests.get(url, headers=headers)
        try:
            mess = ("免费余额："+str(response.json()["total_available"])+"美元");
            return mess
        except:
            mess = "余额获取失败."
            return mess
    except:
        mess = "连接openai出错."
        return mess




    
