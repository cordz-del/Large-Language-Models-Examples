import re

def check_sensitive_content(text):
    # Define regex patterns for sensitive content (adjust patterns as needed)
    patterns = [
        r"\bkill\b", 
        r"\bhate\b", 
        r"\b(?:racist|sexist)\b"
    ]
    flagged = []
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            flagged.append(pattern)
    if flagged:
        print(f"Sensitive content detected for patterns: {flagged}")
        return True
    else:
        print("No sensitive content detected.")
        return False

if __name__ == "__main__":
    sample_output = "This is a racist remark."
    check_sensitive_content(sample_output)
