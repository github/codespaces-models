#!/bin/bash
SCRIPT_DIR=$(dirname $0)
PAYLOAD_FILE="payload.json"
IMAGE_DATA="`cat \"${SCRIPT_DIR}/sample.png\" | base64`"
echo '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that describes images in details."
            },
            {
                "role": "user",
                "content": [{"text": "What''s in this image?", "type": "text"}, {"image_url": {"url":"data:image/png;base64,'"${IMAGE_DATA}"'","detail":"low"}, "type": "image_url"}]
            }
        ],
        "model": "openai/gpt-4o-mini"
    }' > "$PAYLOAD_FILE"

curl -X POST "https://models.github.ai/inference/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d @payload.json
echo
rm -f "$PAYLOAD_FILE"