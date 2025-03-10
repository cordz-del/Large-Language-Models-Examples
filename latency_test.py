import time
import requests

def measure_latency(url, payload):
    start_time = time.time()
    response = requests.post(url, json=payload)
    latency = time.time() - start_time
    print(f"Inference latency: {latency:.3f} seconds")
    return latency

if __name__ == "__main__":
    # Example endpoint and payload (update these with your actual model/endpoint)
    test_url = "https://your-ai-endpoint.com/generate"
    test_payload = {"prompt": "Tell me a story about a brave knight."}
    measure_latency(test_url, test_payload)
