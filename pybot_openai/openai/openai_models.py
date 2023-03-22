
import requests

api_key="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"
#api_key="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"
#url = "https://api.openai.com/v1/models"
URL = "https://api.openai.com/v1/models/text-davinci-003"
headers={
        "Host":"api.openai.com",
        "Authorization": "Bearer {}".format(api_key),
        #"User-Agent": "Apifox/1.0.0 (https://www.apifox.cn)",
        #"Accept": "*/*",
        "Host":"api.openai.com",
        "Connection": "keep-alive"
    }
try:
    backmsg = requests.post(url = URL ,headers = headers)#,timeout = (3,7)
except:
    backmsg = "ERROR!"
##    for i in range(4):
##        try:
##            backmsg = requests.post(url = url ,headers = headers ,timeout = 5)
##            if backmsg.choices[0].text != "":
##                break
##        except:
##            continue;
print(backmsg)
