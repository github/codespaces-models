"""This sample demonstrates a multi-turn conversation with the chat completion API.
When using the model for a chat application, you'll need to manage the history of that
conversation and send the latest messages to the model.
"""

import os
from mistralai import Mistral

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# Pick one of the Mistral models from the GitHub Models service
model_name = "Mistral-small"

# Create a client
client = Mistral(api_key=token, server_url=endpoint)

# Call the chat completion API
response = client.chat.complete(
    model=model_name,
    messages=[
        {"role":"system", "content":"You are a helpful assistant."},
        {"role":"user", "content":"What is the capital of France?"},
        {"role":"assistant", "content":"The capital of France is Paris."},
        {"role":"user", "content":"What about Spain?"},
    ],
)

# Print the response
print(response.choices[0].message.content)
