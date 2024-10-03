from openai import AzureOpenAI
import os

client = AzureOpenAI(
    azure_endpoint="https://azure-services-fair-openai1-southcentralus.azure-api.net",
    api_key=os.environ["OPENAI_API_KEY"],
    api_version="2024-06-01"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant"},
        {"role": "user", "content": "Tell me some joke about Generative AI?"}
    ],
    temperature=0.0
)
print(response.choices[0].message.content)