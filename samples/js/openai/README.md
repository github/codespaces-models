# GitHub Models Samples for OpenAI JavaScript SDK

This folder contains samples that leverage the OpenAI JavaScript SDK with the GitHub Models endpoint.

This codespace comes with dependencies pre-installed. If you want to use this code outside of this codespace, install OpenAI SDK using `npm`:

```shell
npm install openai
```

## Running a sample

To run a JavaScript sample, run a command like the following in your terminal:

```shell
node samples/js/openai/multi_turn.js
```

* [basic.js](basic.js): basic call to the gpt-4o-mini chat completion API
* [multi_turn.js](multi_turn.js): multi-turn conversation with the chat completion API
* [streaming.js](streaming.js): generate a response in streaming mode, token by token