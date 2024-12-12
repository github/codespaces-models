"""This sample demonstrates how to use Azure AI Foundry SDK to run GitHub model catalog with evaluation.
It is leveraging your endpoint and key. The call is synchronous.

For those who have Azure credentials, you can run the risk and safety evaluators from Azure AI.

Azure Evaluation SDK: https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/evaluate-sdk
"""

import os
import json
from pathlib import Path
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.ai import evaluation
from azure.ai.evaluation import RougeType, evaluate
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential


token = os.environ['GITHUB_TOKEN']

# Target model is the model to be evaluated.
target_model_name = "Mistral-small"
target_model_endpoint = "https://models.inference.ai.azure.com"
# Judge model is the model to evaluate the target model.
judge_model_name = "gpt-4o-mini"
judge_model_endpoint = "https://models.inference.ai.azure.com"

evaluation_name = "GitHub models evaluation"
eval_data_file = Path("./eval_data.jsonl")
eval_result_file_perf_and_quality = Path("./eval_result_perf_and_quality.json")
eval_result_file_risk_and_safety = Path("./eval_result_risk_and_safety.json")


def generate_eval_data():
    eval_data_queries = [{
        "query": "What is the capital of France?",
        "ground_truth": "Paris",
    }, {
        "query": "Where is Wineglass Bay?",
        "ground_truth": "Wineglass Bay is located on the Freycinet Peninsula on the east coast of Tasmania, Australia.",
    }]

    with eval_data_file.open("w") as f:
        for eval_data_query in eval_data_queries:
            client = ChatCompletionsClient(
                endpoint=target_model_endpoint,
                credential=AzureKeyCredential(token),
            )

            context = "You are a geography teacher."
            response = client.complete(
                messages=[
                    SystemMessage(content=context),
                    UserMessage(content=eval_data_query["query"]),
                ],
                model=target_model_name,
                temperature=1.,
                max_tokens=1000,
                top_p=1.    
            )
            result = response.choices[0].message.content

            eval_data = {
                "id": "1",
                "description": "Evaluate the model",
                "query": eval_data_query["query"],
                "context": context,
                "response": result,
                "ground_truth": eval_data_query["ground_truth"],
            }
            f.write(json.dumps(eval_data) + "\n")


def run_perf_and_quality_evaluators():
    model_config = {
        "azure_endpoint": judge_model_endpoint,
        "azure_deployment": judge_model_name,
        "api_key": token,
    }

    evaluators = {
        "BleuScoreEvaluator": evaluation.BleuScoreEvaluator(),
        "F1ScoreEvaluator": evaluation.F1ScoreEvaluator(),
        "GleuScoreEvaluator": evaluation.GleuScoreEvaluator(),
        "MeteorScoreEvaluator": evaluation.MeteorScoreEvaluator(),
        "RougeScoreEvaluator": evaluation.RougeScoreEvaluator(rouge_type=RougeType.ROUGE_L),
        "CoherenceEvaluator": evaluation.CoherenceEvaluator(model_config=model_config),
        "FluencyEvaluator": evaluation.FluencyEvaluator(model_config=model_config),
        "GroundednessEvaluator": evaluation.GroundednessEvaluator(model_config=model_config),
        "QAEvaluator": evaluation.QAEvaluator(model_config=model_config, _parallel=False),
        "RelevanceEvaluator": evaluation.RelevanceEvaluator(model_config=model_config),
        "RetrievalEvaluator": evaluation.RetrievalEvaluator(model_config=model_config),
        "SimilarityEvaluator": evaluation.SimilarityEvaluator(model_config=model_config),
    }

    eval_results = evaluate(
        data=eval_data_file,
        evaluators=evaluators,
        evaluation_name=evaluation_name,
        target=None,
        output_path=eval_result_file_perf_and_quality,
    )
    print(json.dumps(eval_results, indent=4))


def run_risk_and_safety_evaluators_with_azure():
    azure_ai_project = {
        "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
        "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP_NAME"),
        "project_name": os.environ.get("AZURE_PROJECT_NAME"),
    }
    credential = DefaultAzureCredential()
    evaluators = {
        "ContentSafetyEvaluator": evaluation.ContentSafetyEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "HateUnfairnessEvaluator": evaluation.HateUnfairnessEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "SelfHarmEvaluator": evaluation.SelfHarmEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "SexualEvaluator": evaluation.SexualEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "ViolenceEvaluator": evaluation.ViolenceEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "ProtectedMaterialEvaluator": evaluation.ProtectedMaterialEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "IndirectAttackEvaluator": evaluation.IndirectAttackEvaluator(azure_ai_project=azure_ai_project, credential=credential),
        "GroundednessProEvaluator": evaluation.GroundednessProEvaluator(azure_ai_project=azure_ai_project, credential=credential),
    }

    risk_and_safety_result_dict = {}
    with eval_data_file.open("r") as f:
        for line in f:
            eval_data = json.loads(line)
            for name, evaluator in evaluators.items():
                if name != "GroundednessProEvaluator":
                    score = evaluator(query=eval_data["query"], response=eval_data["response"])
                else:
                    score = evaluator(query=eval_data["query"], response=eval_data["response"], context=eval_data["context"])
                print(f"{name}: {score}")
                risk_and_safety_result_dict[name] = score

    with eval_result_file_risk_and_safety.open("w") as f:
        f.write(json.dumps(risk_and_safety_result_dict, indent=4))


if __name__ == "__main__":
    # Generate evaluation data with GitHub model catalog and save it to a file.
    generate_eval_data()

    # Run performance and quality evaluators with GitHub model catalog.
    run_perf_and_quality_evaluators()

    # # Uncomment the following code with Azure credentials, then we can run the risk and safety evaluators from Azure AI.
    # run_risk_and_safety_evaluators_with_azure()
