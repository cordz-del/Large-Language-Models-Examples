# Use the Hugging Face Transformers pipeline to streamline text generation.
# This snippet highlights the simplicity and power of the pipeline API for rapid prototyping.
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2")
output = generator("Once upon a time", max_length=50, num_return_sequences=1)
print("Generated Text:", output)
