# Create a function that utilizes prompt templates to dynamically generate content.
# This illustrates a sophisticated prompt engineering technique, emphasizing versatility in content creation.
def generate_story(prompt_template, theme):
    prompt = prompt_template.format(theme=theme)
    generated = generator(prompt, max_length=120, temperature=0.8)
    return generated[0]['generated_text']

template = "Compose a short story about a {theme} adventure."
story = generate_story(template, theme="space exploration")
print("Generated Story:", story)
