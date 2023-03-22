import requests
import urllib.parse

api_key="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"
url = "https://api.openai.com/v1/completions"
msg = "Hello World! --sid10t."
data={
"model": "text-davinci-003",
"prompt": "Say this is a test",
"temperature": 0,
"max_tokens": 7
}
#urllib.parse.quote(data,encoding="utf-8")
headers={
"Content-Type": "application/json",
"Authorization": "Bearer "+api_key,
}
try:
	#headers = random.choice(headers_list)
	backmsg = requests.post(url=url,headers=headers,data=data,timeout=5)
except:
	backmsg = "ERROR!"
	for i in range(4):
	#headers = random.choice(headers_list)
		try:
			backmsg = requests.post(url=url,headers=headers,data=data,timeout=5)
			if backmsg.choices[0].text != "":
				break
		except:
			continue;
print(backmsg)
