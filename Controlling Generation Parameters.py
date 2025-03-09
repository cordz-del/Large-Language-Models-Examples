# This snippet shows how to fine-tune generation parameters like temperature and top_k
# to balance creativity and coherence in the output.
prompt = "Describe a bustling city at night in vivid detail:\n"
generated = generator(prompt, max_length=100, temperature=0.9, top_k=50, num_return_sequences=1)
print("Detailed Description:", generated[0]['generated_text'])
