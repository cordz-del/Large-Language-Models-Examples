# Build a simple Q&A function by constructing a prompt that mimics a question-answer format.
# This demonstrates how prompt engineering can be leveraged for interactive applications.
def answer_question(question):
    prompt = f"Q: {question}\nA:"
    generated = generator(prompt, max_length=60, temperature=0.5)
    # Extract the answer part from the generated text.
    return generated[0]['generated_text'].split("A:")[-1].strip()

question = "What is the significance of prompt engineering in AI?"
answer = answer_question(question)
print("Answer:", answer)
