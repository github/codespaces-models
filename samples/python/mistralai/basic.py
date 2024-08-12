"""This sample demonstrates a basic call to the chat completion API.
It is leveraging your endpoint and key. The call is synchronous."""

import os
from mistralai import Mistral

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# Pick one of the Mistral models from the GitHub Models service
model_name = "Mistral-small"

client = Mistral(api_key=token, server_url=endpoint)

response = client.chat.complete(
    model=model_name,
    messages=[
        {"role":"system", "content":"You are a helpful assistant."},
        {"role":"user", "content":"What is the capital of France?"},
    ],
    # Optional parameters
    temperature=1.,
    max_tokens=1000,
    top_p=1.    
)

print(response.choices[0].message.content)
