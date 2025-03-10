import time
import requests

def measure_batch_latency(url, payload, iterations=10):
    latencies = []
    for _ in range(iterations):
        start = time.time()
        response = requests.post(url, json=payload)
        latencies.append(time.time() - start)
    avg_latency = sum(latencies) / len(latencies)
    print(f"Average latency over {iterations} iterations: {avg_latency:.3f} seconds")
    return avg_latency

if __name__ == "__main__":
    test_url = "https://your-ai-endpoint.com/generate"
    test_payload = {"prompt": "Describe the future of technology."}
    measure_batch_latency(test_url, test_payload)
