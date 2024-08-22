"""A language model can be given a set of tools it can invoke,
for running specific actions depending on the context of the conversation.
This sample demonstrates how to define a function tool and how to act on a request from the model to invoke it."""

import os
import json
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


# Define a function that returns flight information between two cities (mock implementation)
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


# Define a function tool that the model can ask to invoke in order to retrieve flight information
tool = {
    "type": "function",
    "function": {
        "name": "get_flight_info",
        "description": """Returns information about the next flight between two cities.
            This includes the name of the airline, flight number and the date and time
            of the next flight""",
        "parameters": {
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
    },
}


messages = [
    {
        "role": "system",
        "content": "You an assistant that helps users find flight information.",
    },
    {
        "role": "user",
        "content": "I'm interested in going to Miami. What is the next flight there from Seattle?",
    },
]

response = client.chat.completions.create(
    messages=messages,
    tools=[tool],
    model=model_name,
)

# We expect the model to ask for a tool call
if response.choices[0].finish_reason == "tool_calls":

    # Append the model response to the chat history
    messages.append(response.choices[0].message)

    # We expect a single tool call
    if (
        response.choices[0].message.tool_calls
        and len(response.choices[0].message.tool_calls) == 1
    ):

        tool_call = response.choices[0].message.tool_calls[0]

        # We expect the tool to be a function call
        if tool_call.type == "function":

            # Parse the function call arguments and call the function
            function_args = json.loads(tool_call.function.arguments.replace("'", '"'))
            print(
                f"Calling function `{tool_call.function.name}` with arguments {function_args}"
            )
            callable_func = locals()[tool_call.function.name]
            function_return = callable_func(**function_args)
            print(f"Function returned = {function_return}")

            # Append the function call result fo the chat history
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": tool_call.function.name,
                    "content": function_return,
                }
            )

            # Get another response from the model
            response = client.chat.completions.create(
                messages=messages,
                tools=[tool],
                model=model_name,
            )

            print(f"Model response = {response.choices[0].message.content}")