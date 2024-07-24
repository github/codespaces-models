"""This sample demonstrates a basic call to the chat completion API.
It is leveraging your endpoint and key. The call is synchronous."""

import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Ensure the GITHUB_TOKEN environment variable is set
assert "GITHUB_TOKEN" in os.environ, "Please set the GITHUB_TOKEN environment variable."
github_token = os.environ["GITHUB_TOKEN"]

# We can use some defaults for the other two variables
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"

# Create a client
client = MistralClient(api_key=github_token, endpoint=endpoint)

# Call the chat completion API
response = client.chat(
    model=model_name,
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="What is the capital of France?"),
    ],
)

# Print the response
print(response.choices[0].message.content)