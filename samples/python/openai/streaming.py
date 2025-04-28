"""For a better user experience, you will want to stream the response of the model
so that the first token shows up early and you avoid waiting for long responses."""

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"

# Pick one of the Azure OpenAI models from the GitHub Models service
model_name = "openai/gpt-4o-mini"

# Create a client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Call the chat completion API
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Give me 5 good reasons why I should exercise every day.",
        },
    ],
    model=model_name,
    stream=True,
)

# Print the streamed response
for update in response:
    if update.choices[0].delta.content:
        print(update.choices[0].delta.content, end="")

print()