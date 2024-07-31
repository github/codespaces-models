# GitHub Models Samples - Python

This folder contains samples for interacting with GitHub Models using Python.

Multiple model-specific SDKs are compatible with the endpoint served under the GitHub Models catalog, such as `openai` and `mistralai` packages for their respective models. This makes it easy to port your currently existing code using one of those SDKs.

You can also use the `azure-ai-inference` package for a cross-model unified SDK.

## SDKs

- [openai](./openai/README.md) (works with all Azure OpenAI models)
- [azure-ai-inference](./azure_ai_inference/README.md) (works with all models)
- [mistral](./mistralai/README.md) (works with all Mistral AI models)

## Running a sample

To run a Python sample, run the following command in your terminal:

```shell
python samples/python/azure_ai_inference/multi_turn.py
```

## Running a cookbook

To run a [Python cookbook](../../cookbooks/python/README.md), simply open one in your IDE and execute the code cells.
