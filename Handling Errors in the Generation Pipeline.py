# Incorporate error handling to manage unexpected issues during text generation.
# Robust error handling is essential for production-level applications.
try:
    prompt = "Generate a creative story involving dragons and wizards."
    generated = generator(prompt, max_length=100)
    print("Generated Story:", generated[0]['generated_text'])
except Exception as e:
    print("An error occurred during text generation:", str(e))
