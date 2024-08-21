# GitHub Models Samples for OpenAI Python SDK

This folder contains samples that leverage the OpenAI Python SDK with the GitHub Models endpoint. Samples are available as Jupyter notebooks and as Python scripts.

## Jupyter Notebooks

To run these notebooks, click on a link below to open it in Codespaces and select a Python3 kernel.

* [getting_started.ipynb](getting_started.ipynb). Basic interaction, multi-turn conversations, image inputs, streamed responses, Functions API.
* [embeddings_getting_started.ipynb](embeddings_getting_started.ipynb): create embeddings for strings using the `text-embedding-3-small` model

## Python Scripts

To run these scripts, open your terminal and run a command like:

```shell
python3 samples/python/openai/basic.py
```

* [basic.py](basic.py): basic call to the gpt-4o-mini chat completion API
* [chat_with_image_file.py](chat_with_image_file.py): image file as input
* [multi_turn.py](multi_turn.py): multi-turn conversation with the chat completion API
* [streaming.py](streaming.py): generate a response in streaming mode, token by token
* [tools.py](tools.py): run specific actions depending on the context of the conversation with the functions API
