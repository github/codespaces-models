"""This sample demonstrates a basic call to the chat completion API.
It is leveraging your endpoint and key. The call is synchronous."""

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
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        },
    ],
    model=model_name,
)

# Print the response
print(response.choices[0].message.content)
