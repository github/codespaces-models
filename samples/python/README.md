# GitHub Models Samples - Python

This folder contains samples for interacting with GitHub Models using Python.

Multiple model-specific SDKs are compatible with the endpoint served under the GitHub Models catalog, such as [`openai`](./openai/README.md) and [`mistralai`](./mistralai/README.md) packages for their respective models. This makes it easy to port your existing code using one of those SDKs.

You can also use the [`azure-ai-inference`](./azure_ai_inference/README.md) package for a cross-model unified SDK.

## SDKs
- [`openai`](./openai/chat_getting_started.ipynb)
- [`azure-ai-inference`](./azure_ai_inference/README.md)
- [`mistralai`](./mistralai/README.md)

## Running a sample

To run a Python sample, run the following command in your terminal:

```bash
# To run the multi-turn sample using the Azure AI Inference SDK:
$ python samples/python/azure_ai_inference/multi_turn.py
```
