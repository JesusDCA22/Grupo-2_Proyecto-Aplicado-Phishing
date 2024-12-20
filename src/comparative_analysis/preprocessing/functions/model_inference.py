import json
import httpx
import boto3
from botocore.exceptions import ClientError

class ModelInference:
    def __init__(self, region_name="us-east-1"):
        self.client = boto3.client("bedrock-runtime", region_name=region_name)

    def obtener_respuesta(self, user_message, option_model, max_retries=3, delay=5):
        if option_model == 1:
            model_id = "mistral.mistral-large-2402-v1:0"
            conversation = [
                {
                    "role": "user",
                    "content": [{"text": user_message}],
                }
            ]

            try:
                response = self.client.converse(
                    modelId=model_id,
                    messages=conversation,
                    inferenceConfig={"maxTokens": 2000, "temperature": 0.5, "topP": 0.9},
                )
                response_text = response["output"]["message"]["content"][0]["text"]
                return response_text
            except httpx.HTTPError as e:
                print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
                return None

        if option_model == 2:
            model_id = "meta.llama3-70b-instruct-v1:0"
            formatted_prompt = f"""
            <|begin_of_text|><|start_header_id|>user<|end_header_id|>
            {user_message}
            <|eot_id|>
            <|start_header_id|>assistant<|end_header_id|>
            """

            native_request = {
                "prompt": formatted_prompt,
                "max_gen_len": 1000,
                "temperature": 0.5,
            }

            request = json.dumps(native_request)

            try:
                response = self.client.invoke_model(modelId=model_id, body=request)
                model_response = json.loads(response["body"].read())
                response_text = model_response["generation"]
                return response_text
            except (ClientError, Exception) as e:
                print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
                return None
