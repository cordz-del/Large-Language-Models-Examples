from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

def analyze_text_quality(text):
    # Toxicity keyword check
    toxic_keywords = ["hate", "kill", "stupid"]
    toxic_found = [word for word in toxic_keywords if word in text.lower()]
    
    # Bias check
    bias_terms = ["always", "never"]
    bias_found = [term for term in bias_terms if term in text.lower()]
    
    # Sentiment analysis
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    
    report = {
        "text": text,
        "toxic": bool(toxic_found),
        "toxic_keywords": toxic_found,
        "biased": bool(bias_found),
        "bias_terms": bias_found,
        "sentiment": sentiment
    }
    return report

if __name__ == "__main__":
    outputs = [
        "I absolutely love this product!",
        "This is stupid and I hate it.",
        "They always do this, it's unbelievable."
    ]
    reports = [analyze_text_quality(text) for text in outputs]
    for rep in reports:
        print(rep)
