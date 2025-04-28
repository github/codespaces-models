import MistralClient from '@mistralai/mistralai';

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.github.ai/inference/";

/* Pick one of the Mistral models from the GitHub Models service */
const modelName = "mistral-ai/Mistral-small";

export async function main() {

  const client = new MistralClient(token, endpoint);

  const response = await client.chatStream({
    model: modelName,
    messages: [
      { role:"system", content: "You are a helpful assistant." },
      { role:"user", content: "Give me 5 good reasons why I should exercise every day." }
    ],
  });

  for await (const chunk of response) {
    if (chunk.choices[0].delta.content !== undefined) {
      const streamText = chunk.choices[0].delta.content;
      process.stdout.write(streamText);
    }
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});