def check_toxicity(text):
    toxic_keywords = ["hate", "kill", "stupid", "idiot", "nazi"]
    found_keywords = [word for word in toxic_keywords if word in text.lower()]
    if found_keywords:
        print(f"Toxic keywords found: {found_keywords}")
        return True
    else:
        print("No toxic keywords detected.")
        return False

if __name__ == "__main__":
    sample_output = "I think this idea is stupid and will never work."
    check_toxicity(sample_output)
