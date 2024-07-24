"""For a better user experience, you will want to stream the response of the model
so that the first token shows up early and you avoid waiting for long responses."""

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Ensure the GITHUB_TOKEN environment variable is set
assert "GITHUB_TOKEN" in os.environ, "Please set the GITHUB_TOKEN environment variable."
github_token = os.environ["GITHUB_TOKEN"]

# We can use some defaults for the other two variables
endpoint = "https://models.inference.ai.azure.com"
# Use any model of the catalog, this SDK works with all chat models
model_name = "gpt-4o"

# Create a client
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(github_token),
)

# Call the chat completion API
response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Give me 5 good reasons why I should exercise every day."),
    ],
    model=model_name,
)

# Print the streamed response
for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
