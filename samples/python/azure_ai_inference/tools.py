"""A language model can be given a set of tools it can invoke,
for running specific actions depending on the context of the conversation.
This sample demonstrates how to define a function tool and how to act on a request from the model to invoke it."""

import os
import json
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    AssistantMessage,
    ChatCompletionsToolCall,
    ChatCompletionsToolDefinition,
    CompletionsFinishReason,
    FunctionDefinition,
    SystemMessage,
    ToolMessage,
    UserMessage,
)
from azure.core.credentials import AzureKeyCredential

assert "GITHUB_TOKEN" in os.environ, "Please set the GITHUB_TOKEN environment variable."
token = os.environ["GITHUB_TOKEN"]

endpoint = "https://models.github.ai/inference"

# By using the Azure AI Inference SDK, you can easily experiment with different models
# by modifying the value of `modelName` in the code below. For this code sample
# you need a model supporting tools. The following compatible models are
# available in the GitHub Models service:
# 
# Cohere: Cohere-command-r, Cohere-command-r-plus
# Mistral AI: Mistral-large, Mistral-large-2407, Mistral-Nemo, Mistral-small
# Azure OpenAI: gpt-4o-mini, gpt-4o
model_name = "openai/gpt-4o-mini"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def get_flight_info(origin_city: str, destination_city: str):
    if origin_city == "Seattle" and destination_city == "Miami":
        return json.dumps(
            {
                "airline": "Delta",
                "flight_number": "DL123",
                "flight_date": "May 7th, 2024",
                "flight_time": "10:00AM",
            }
        )
    return json.dump({"error": "No flights found between the cities"})

flight_info = ChatCompletionsToolDefinition(
    function=FunctionDefinition(
        name="get_flight_info",
        description="""Returns information about the next flight between two cities.
            This includes the name of the airline, flight number and the date and
            time of the next flight""",
        parameters={
            "type": "object",
            "properties": {
                "origin_city": {
                    "type": "string",
                    "description": "The name of the city where the flight originates",
                },
                "destination_city": {
                    "type": "string",
                    "description": "The flight destination city",
                },
            },
            "required": ["origin_city", "destination_city"],
        },
    )
)


messages = [
    SystemMessage(content="You an assistant that helps users find flight information."),
    UserMessage(
        content="I'm interested in going to Miami. What is the next flight there from Seattle?"
    ),
]

response = client.complete(
    messages=messages,
    tools=[flight_info],
    model=model_name,
)

if response.choices[0].finish_reason == CompletionsFinishReason.TOOL_CALLS:

    messages.append(AssistantMessage(tool_calls=response.choices[0].message.tool_calls))

    if (
        response.choices[0].message.tool_calls
        and len(response.choices[0].message.tool_calls) == 1
    ):

        tool_call = response.choices[0].message.tool_calls[0]

        if isinstance(tool_call, ChatCompletionsToolCall):

            function_args = json.loads(tool_call.function.arguments.replace("'", '"'))
            print(
                f"Calling function `{tool_call.function.name}` with arguments {function_args}"
            )
            callable_func = locals()[tool_call.function.name]
            function_return = callable_func(**function_args)
            print(f"Function returned = {function_return}")

            messages.append(
                ToolMessage(tool_call_id=tool_call.id, content=function_return)
            )

            response = client.complete(
                messages=messages,
                tools=[flight_info],
                model=model_name,
            )

            print(f"Model response = {response.choices[0].message.content}")