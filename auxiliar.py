from openai import OpenAI

client = OpenAI(api_key= "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")

models = client.models.list()
print(models)