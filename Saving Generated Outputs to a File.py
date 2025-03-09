# Save the generated text to a file for logging or further analysis.
# This snippet highlights best practices in maintaining records of model outputs.
output_text = generator("Once upon a time in a distant galaxy", max_length=80)[0]['generated_text']
with open("generated_output.txt", "w") as f:
    f.write(output_text)
print("Output saved to generated_output.txt")
