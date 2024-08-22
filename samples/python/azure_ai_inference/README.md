# GitHub Models Samples for Azure AI Inference SDK

This folder contains samples that leverage the Azure AI Inference Python SDK with the GitHub Models endpoint.

## Jupyter Notebooks

To run these notebooks, click on a link below to open it in Codespaces and select a Python3 kernel.

* [getting_started.ipynb](getting_started.ipynb). Basic interaction, multi-turn conversations, image inputs, streamed responses, Functions API.

## Running a sample

To run these scripts, open your terminal and run a command like:

```shell
python3 samples/python/azure_ai_inference/basic.py
```

* [basic.py](basic.py): basic call to the gpt-4o-mini chat completion API
* [multi_turn.py](multi_turn.py): multi-turn conversation with the chat completion API
* [streaming.py](streaming.py): generate a response in streaming mode, token by token
