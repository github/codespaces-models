"""For a better user experience, you will want to stream the response of the model
so that the first token shows up early and you avoid waiting for long responses."""

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
response = client.chat_stream(
    model=model_name,
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(
            role="user",
            content="Give me 5 good reasons why I should exercise every day.",
        ),
    ],
)

# Print the streamed response
for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

print()