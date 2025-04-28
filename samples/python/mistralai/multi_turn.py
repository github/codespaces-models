"""This sample demonstrates a multi-turn conversation with the chat completion API.
When using the model for a chat application, you'll need to manage the history of that
conversation and send the latest messages to the model.
"""

import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"

# Pick one of the Mistral models from the GitHub Models service
model_name = "Mistral-small"

# Create a client
client = MistralClient(api_key=token, endpoint=endpoint)

# Call the chat completion API
response = client.chat(
    model=model_name,
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="What is the capital of France?"),
        ChatMessage(role="assistant", content="The capital of France is Paris."),
        ChatMessage(role="user", content="What about Spain?"),
    ],
)

# Print the response
print(response.choices[0].message.content)
