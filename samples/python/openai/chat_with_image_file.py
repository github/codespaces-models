"""This model supports using images as inputs. To run a chat completion using
a local image file, use the following sample."""

import os
import base64
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# Pick one of the Azure OpenAI models from the GitHub Models service
model_name = "gpt-4o-mini"

# Create a client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def get_image_data_url(image_file: str, image_format: str) -> str:
    """
    Helper function to converts an image file to a data URL string.
    Args:
        image_file (str): The path to the image file.
        image_format (str): The format of the image file.
    Returns:
        str: The data URL of the image.
    """
    try:
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"Could not read '{image_file}'.")
        exit()
    return f"data:image/{image_format};base64,{image_data}"


# Call the chat completion API
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that describes images in detail.",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        # using a file located in this directory
                        "url": get_image_data_url(
                            os.path.join(os.path.dirname(__file__), "sample.png"), "png"
                        )
                    },
                },
            ],
        },
    ],
    model=model_name,
)

# Print the response
print(response.choices[0].message.content)