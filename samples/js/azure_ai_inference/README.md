# GitHub Models Samples for Azure AI Inference JavaScript SDK

This folder contains samples that leverage the Azure AI Inference JavaScript SDK with the GitHub Models endpoint. The Azure AI Inference JavaScript SDK supports a wide range of models, so it's easy to adapt these samples to use a different model by changing the value of:

```js
const modelName = "MODEL";
```

This codespace comes with dependencies pre-installed. If you want to use this code outside of this codespace, install the Azure AI Inference SDK using `npm`:

```shell
npm install @azure-rest/ai-inference @azure/core-auth @azure/core-sse
```

## Running a sample

To run a JavaScript sample, run a command like the following in your terminal:

```shell
node samples/js/azure_ai_inference/multi_turn.js
```

* [basic.js](basic.js): basic call to the gpt-4o-mini chat completion API
* [multi_turn.js](multi_turn.js): multi-turn conversation with the chat completion API
* [streaming.js](streaming.js): generate a response in streaming mode, token by token