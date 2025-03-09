# Demonstrate prompt engineering by explicitly guiding the LLM to generate creative content.
# Adjusting the prompt helps steer the model's output toward desired styles or topics.
prompt = "Write a poem about the beauty of nature:\n"
generated = generator(prompt, max_length=80, temperature=0.7, top_p=0.95)
print("Prompt Engineered Poem:", generated[0]['generated_text'])
