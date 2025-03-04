import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_chat_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    prompt = "Can you explain how transformers work in natural language processing?"
    answer = generate_chat_response(prompt)
    print("Response from LLM:", answer)
