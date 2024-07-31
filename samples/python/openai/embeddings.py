import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# Pick one of the OpenAI embeddings models from the GitHub Models service
model_name = "text-embedding-3-small"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.embeddings.create(
    input=["first phrase", "second phrase", "third phrase"],
    model=model_name,
)

for item in response.data:
    length = len(item.embedding)
    print(
        f"data[{item.index}]: length={length}, "
        f"[{item.embedding[0]}, {item.embedding[1]}, "
        f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
    )
print(response.usage)
