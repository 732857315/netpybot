import openai

openai.api_key = "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"


msg="请说出一个中文"
print("测试问题："+msg)
try:
    response = openai.Completion.create(
        model="gpt-3.5-turbo", # text-davinci-003 gpt-3.5-turbo-0301
        messages=[
            #{"role":"system","content":msg},
            #{"role":"assistant","content":msg},
            {"role":"user","content":msg}
        ]# 用户提供的输入文本，用于指导GPT输出
    )
    print(response["choices"][0]["message"]["content"])
except:
    print("连接openai出错.")
