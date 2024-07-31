import os

from azure.ai.inference import EmbeddingsClient
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# By using the Azure AI Inference SDK, you can easily experiment with different models
# by modifying the value of `modelName` in the code below. For this code sample
# you need an embedding model. The following embedding models are
# available in the GitHub Models service:
# 
# Cohere: Cohere-embed-v3-english, Cohere-embed-v3-multilingual
# Azure OpenAI: text-embedding-3-small, text-embedding-3-large
model_name = "text-embedding-3-small"

client = EmbeddingsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token)
)

response = client.embed(
    input=["first phrase", "second phrase", "third phrase"],
    model=model_name
)

for item in response.data:
    length = len(item.embedding)
    print(
        f"data[{item.index}]: length={length}, "
        f"[{item.embedding[0]}, {item.embedding[1]}, "
        f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
    )
print(response.usage)
