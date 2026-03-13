"""For a better user experience, you will want to stream the response of the model
so that the first token shows up early and you avoid waiting for long responses."""

import os
from mistralai import Mistral

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"

# Pick one of the Mistral models from the GitHub Models service
model_name = "mistral-small-2503"

# Create a client
client = Mistral(api_key=token, server_url=endpoint)

# Call the chat completion API
response = client.chat.stream(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Give me 5 good reasons why I should exercise every day.",
        },
    ],
)

# Print the streamed response
for event in response:
    if event.data.choices:
        print(event.data.choices[0].delta.content or "", end="")

print()
