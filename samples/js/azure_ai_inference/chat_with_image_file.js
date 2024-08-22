import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";
import fs from 'fs';
import path from 'path';

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";

/* By using the Azure AI Inference SDK, you can easily experiment with different models
   by modifying the value of `modelName` in the code below. For this code sample
   you need to use a model that supports image inputs. The following image models are
   available in the GitHub Models service:

   Azure OpenAI: gpt-4o-mini, gpt-4o */
const modelName = "gpt-4o-mini";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant that describes images in details." },
        { role: "user", content: [
            { type: "text", text: "What's in this image?"},
            { type: "image_url", image_url: {
                url: getImageDataUrl(path.join(import.meta.dirname, "sample.png"), "png"), details: "low"}}
          ]
        }
      ],
      model: modelName
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }
  console.log(response.body.choices[0].message.content);
}

/**
 * Get the data URL of an image file.
 * @param {string} imageFile - The path to the image file.
 * @param {string} imageFormat - The format of the image file. For example: "jpeg", "png".
 * @returns {string} The data URL of the image.
 */
function getImageDataUrl(imageFile, imageFormat) {
  try {
      const imageBuffer = fs.readFileSync(imageFile);
      const imageBase64 = imageBuffer.toString('base64');
      return `data:image/${imageFormat};base64,${imageBase64}`;
  } catch (error) {
      console.error(`Could not read '${imageFile}'.`);
      console.error('Set the correct path to the image file before running this sample.');
      process.exit(1);
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
