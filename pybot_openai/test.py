from urllib.request import urlopen
import openai
# openai.api_key_path = "./openaikey.txt"
# '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' "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"
openai.api_key = "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"

prompt = "The meaning of life is"

response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

message = response.choices[0].text
print(message)
input()
