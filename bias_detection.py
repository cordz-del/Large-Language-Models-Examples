def detect_bias(text):
    bias_terms = ["always", "never", "all", "none"]
    biased_phrases = [term for term in bias_terms if term in text.lower()]
    if biased_phrases:
        print(f"Biased language detected: {biased_phrases}")
        return True
    else:
        print("No significant bias detected.")
        return False

if __name__ == "__main__":
    sample_output = "They always behave this way."
    detect_bias(sample_output)
