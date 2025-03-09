# Load a pre-trained language model (GPT-2 in this example) and its tokenizer.
# This demonstrates the fundamental step of initializing an LLM using Hugging Face Transformers.
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
print("Loaded GPT-2 model for text generation.")
