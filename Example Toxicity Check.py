def check_for_toxicity(text):
    # Basic example: flag if any toxic keywords appear
    toxic_keywords = ['toxic', 'hate', 'bias']
    return any(keyword in text.lower() for keyword in toxic_keywords)

generated_text = "Your generated response from the LLM..."
assert not check_for_toxicity(generated_text), "The generated text contains toxic content."
