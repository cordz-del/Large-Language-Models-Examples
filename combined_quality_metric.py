from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def compute_quality_score(text):
    # Use sentiment as an indicator (higher compound is better)
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    compound = sentiment["compound"]

    # Check for toxic keywords
    toxic_keywords = ["hate", "kill", "stupid"]
    toxicity = sum([1 for word in toxic_keywords if word in text.lower()])

    # Combine metrics: lower toxicity and higher compound result in a higher score.
    quality_score = compound - (0.5 * toxicity)
    return quality_score

if __name__ == "__main__":
    sample_output = "I hate this product. It is stupid."
    score = compute_quality_score(sample_output)
    print(f"Combined quality score: {score}")
