# This snippet simulates a standalone script (e.g., llm_text_generation_example.py)
# showcasing text generation using an LLM for real-world applications.
if __name__ == "__main__":
    prompt = "In a future world, AI plays a key role in every aspect of life."
    generated = generator(prompt, max_length=100, num_return_sequences=1)
    print("LLM Text Generation Output:", generated)
