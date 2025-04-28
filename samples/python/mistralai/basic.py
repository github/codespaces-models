"""This sample demonstrates a basic call to the chat completion API.
It is leveraging your endpoint and key. The call is synchronous."""

import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"

# Pick one of the Mistral models from the GitHub Models service
model_name = "Mistral-small"

client = MistralClient(api_key=token, endpoint=endpoint)

response = client.chat(
    model=model_name,
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="What is the capital of France?"),
    ],
    # Optional parameters
    temperature=1.,
    max_tokens=1000,
    top_p=1.    
)

print(response.choices[0].message.content)
