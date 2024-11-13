import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pre-trained T5 model and tokenizer
def load_t5_model(model_name='t5-base'):
    """Load T5 model and tokenizer."""
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

# Prepare the input for entity extraction
def prepare_input(text, prefix="extract entities: "):
    """Prepare input text for T5 model with a specified prefix."""
    return prefix + text

# Perform entity extraction
def extract_entities(text, tokenizer, model, max_length=512):
    """Extract entities from text using T5 model."""
    # Prepare the input text
    input_text = prepare_input(text)
    input_ids = tokenizer.encode(input_text, return_tensors='pt', truncation=True, max_length=max_length)

    # Generate the output sequence
    with torch.no_grad():  # Disable gradient calculation for inference
        output_ids = model.generate(input_ids, max_length=max_length)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text

# Load the model and tokenizer
model_name = 't5-base'
tokenizer, model = load_t5_model(model_name)

# Sample text for entity extraction
sample_text = "A 45-year-old lady sought dermatology consultation for severely tender erythematous vesicles and bullae over back, chest and arms."

# Extract entities from the sample text
extracted_entities = extract_entities(sample_text, tokenizer, model)

# Print the extracted entities
print("Extracted Entities:")
print(extracted_entities)