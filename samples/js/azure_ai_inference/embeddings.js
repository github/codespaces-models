import ModelClient from "@azure-rest/ai-inference";
import { isUnexpected } from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";

/* By using the Azure AI Inference SDK, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. For this code sample
   you need an embedding model. The following embedding models are
   available in the GitHub Models service:

   Cohere: Cohere-embed-v3-english, Cohere-embed-v3-multilingual
   Azure OpenAI: text-embedding-3-small, text-embedding-3-large */
const modelName = "text-embedding-3-small";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/embeddings").post({
    body: {
      input: ["first phrase", "second phrase", "third phrase"],
      model: modelName
    }
  });

  if (isUnexpected(response)) {
    throw response.body.error;
  }

  for (const item of response.body.data) {
    let length = item.embedding.length;
    console.log(
	  `data[${item.index}]: length=${length}, ` +
	  `[${item.embedding[0]}, ${item.embedding[1]}, ` +
	  `..., ${item.embedding[length - 2]}, ${item.embedding[length -1]}]`);
  }
  console.log(response.body.usage);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
