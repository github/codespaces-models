"""For a better user experience, you will want to stream the response of the model
so that the first token shows up early and you avoid waiting for long responses."""

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
