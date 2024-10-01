from transformers import AutoModel, AutoTokenizer

model_name = "distilbert-base-uncased"
save_path = "static/distilbert-base-uncased"

# Download the model and tokenizer
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model and tokenizer locally
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

print(f"Model and tokenizer saved to {save_path}")
