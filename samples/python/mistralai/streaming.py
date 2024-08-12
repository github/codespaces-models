"""For a better user experience, you will want to stream the response of the model
so that the first token shows up early and you avoid waiting for long responses."""

import os
from mistralai import Mistral

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# Pick one of the Mistral models from the GitHub Models service
model_name = "Mistral-small"

# Create a client
client = Mistral(api_key=token, server_url=endpoint)

# Call the chat completion API
response = client.chat.stream(
    model=model_name,
    messages=[
        {"role":"system", "content":"You are a helpful assistant."},
        {"role":"user", "content":"Give me 5 good reasons why I should exercise every day."},
    ],
)

# Print the streamed response
if response is not None:
    for update in response:
        content_chunk = update.data.choices[0].delta.content
        if content_chunk:
            print(content_chunk, end="")

print()