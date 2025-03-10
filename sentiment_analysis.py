from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    print(f"Sentiment scores: {scores}")
    return scores

if __name__ == "__main__":
    sample_output = "I absolutely love this innovative idea!"
    analyze_sentiment(sample_output)
