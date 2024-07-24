"""This sample demonstrates a multi-turn conversation with the chat completion API.
When using the model for a chat application, you'll need to manage the history of that
conversation and send the latest messages to the model.
"""

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
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
messages = [
    SystemMessage(content="You are a helpful assistant."),
    UserMessage(content="What is the capital of France?"),
    AssistantMessage(content="The capital of France is Paris."),
    UserMessage(content="What about Spain?"),
]

response = client.complete(messages=messages, model=model_name)

# Print the response
print(response.choices[0].message.content)
