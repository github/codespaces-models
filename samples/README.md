# GitHub Models Samples

This folder contains samples for interacting with GitHub Models. Each subfolder contains examples for a specific language: JavaScript, Python, and cURL.

## Languages

We provide samples in the following languages:

- [JavaScript](js/README.md)
- [Python](python/README.md)
- [cURL](curl/README.md)

## Things to try

Use this Codespace to edit the samples and see what happens! Here are a few suggestions of things you can try.

### Try a different model

Try switching to a different model by finding a line like the one below and changing the model selected. You can find other models to try at [GitHub Marketplace](https://github.com/marketplace/models).

```json
        "model": "gpt-4o-mini"
```

### Try a different prompt

Try a different input to the model (prompt) by changing the text following `"content":` in the lines below. Some examples provide multiple turns of conversation history, and you can modify those too.

```json
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
```

### Change the way the model responds

Some (but not all) models allow you to modify the "system prompt", which does not generate a response directly but changes the *way* the model responds. You can modifying the system prompt by finding a section like the lines below and changing the `"content":` value.

```json
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
```
