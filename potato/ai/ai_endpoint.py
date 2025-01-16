import requests

class AIEndpointClient:
    def __init__(self, endpoint: str, api_key: str):
        self.endpoint = endpoint
        self.api_key = api_key

    def get_ai_response(self, message: str) -> str:
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"message": message},
        )
        return response.json()["response"]


def get_ai_endpoint(config: dict):
    # Check what kind of endpoint the admin was requested
    if 'ai_endpoint' in config:
        endpoint_type = config["ai_endpoint"]
        if endpoint_type == "ollama":

            # Only do the import if we need it prevent unnecessary imports on small systems
            from ollama_endpoint import OllamaEndpoint

            return OllamaEndpoint(config["ai_endpoint"])

    raise ValueError(f"Unknown endpoint type: {endpoint_type}")
