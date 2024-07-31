import OpenAI from "openai";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";

/* Pick one of the OpenAI embeddings models from the GitHub Models service */
const modelName = "text-embedding-3-small";

export async function main() {

  const client = new OpenAI({ baseURL: endpoint, apiKey: token });

  const response = await client.embeddings.create({
	input: ["first phrase", "second phrase", "third phrase"],
	model: modelName     
  });

  for (const item of response.data) {
	let length = item.embedding.length;
	console.log(
		`data[${item.index}]: length=${length}, ` +
		`[${item.embedding[0]}, ${item.embedding[1]}, ` +
		`..., ${item.embedding[length - 2]}, ${item.embedding[length -1]}]`);
  }
  console.log(response.usage);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
