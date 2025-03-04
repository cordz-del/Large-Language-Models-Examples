from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline("text-generation", model="gpt2")  # Replace "gpt2" with any other model if desired

# Define a prompt for text generation
prompt = "In the realm of artificial intelligence, large language models are revolutionizing"

# Generate text with specific settings
results = generator(prompt, max_length=100, num_return_sequences=1, temperature=0.8)

print("Generated Text:")
print(results[0]["generated_text"])
