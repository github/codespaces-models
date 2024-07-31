# GitHub Models Samples - JavaScript

This folder contains samples for interacting with GitHub Models using JavaScript.

Multiple model-specific SDKs are compatible with the endpoint served under the GitHub Models catalog, such as [`openai`](./openai/README.md) and [`mistralai`](./mistralai/README.md) packages for their respective models. This makes it easy to port your existing code using one of those SDKs.

You can also use the [`azure-ai-inference`](./azure_ai_inference/README.md) package for a cross-model unified SDK.

## SDKs
- [`openai`](./openai/README.md)
- [`azure-ai-inference`](./azure_ai_inference/README.md)
- [`mistralai`](./mistralai/README.md)

## Running a sample

To run a JavaScript sample, a command like the following in your terminal:

```shell
node samples/js/azure_ai_inference/multi_turn.js
```
