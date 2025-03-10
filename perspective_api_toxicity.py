import requests

def check_toxicity_with_perspective(text):
    API_KEY = "YOUR_API_KEY"
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    payload = {
        "comment": {"text": text},
        "languages": ["en"],
        "requestedAttributes": {"TOXICITY": {}}
    }
    params = {"key": API_KEY}
    response = requests.post(url, params=params, json=payload)
    if response.status_code == 200:
        toxicity_score = response.json()['attributeScores']['TOXICITY']['summaryScore']['value']
        print(f"Perspective API Toxicity Score: {toxicity_score}")
        return toxicity_score
    else:
        print("Error calling Perspective API:", response.text)
        return None

if __name__ == "__main__":
    sample_output = "I hate everything about this!"
    check_toxicity_with_perspective(sample_output)
