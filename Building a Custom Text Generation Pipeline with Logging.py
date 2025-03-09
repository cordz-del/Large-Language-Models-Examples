import logging

# Set up basic logging to track prompts and outputs, which is useful for iterative prompt engineering.
logging.basicConfig(level=logging.INFO, filename='llm_generation.log', filemode='a', format='%(asctime)s - %(message)s')

def custom_text_generation(prompt, max_length=100, temperature=0.8):
    logging.info(f"Prompt: {prompt}")
    generated = generator(prompt, max_length=max_length, temperature=temperature)
    output_text = generated[0]['generated_text']
    logging.info(f"Generated: {output_text}")
    return output_text

final_output = custom_text_generation("Envision a future where technology and nature coexist harmoniously.")
print("Final Generated Output:", final_output)
