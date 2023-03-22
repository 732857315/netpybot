import os
import openai
openai.organization = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
