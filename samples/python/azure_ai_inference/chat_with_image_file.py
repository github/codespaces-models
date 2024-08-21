"""If a model supports using images as inputs, you can run a chat completion
using a local image file, use the following sample."""

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# By using the Azure AI Inference SDK, you can easily experiment with different models
# by modifying the value of `modelName` in the code below. For this code sample
# you need to use a model that supports image inputs. The following image models are
# available in the GitHub Models service:
# 
# Azure OpenAI: gpt-4o-mini, gpt-4o
model_name = "gpt-4o-mini"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file=os.path.join(os.path.dirname(__file__), "sample.png"),
                        image_format="png",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
