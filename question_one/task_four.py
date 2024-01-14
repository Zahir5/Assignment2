import spacy
import os
from transformers import BertTokenizer, BertModel
from collections import Counter
from tqdm import tqdm  

# Load spaCy model
nlp_sci_sm = spacy.load('en_core_sci_sm')

# Load BioBERT tokenizer and model
# tokenizer_bio = BertTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed', do_lower_case=False)
# model_bio = BertModel.from_pretrained('monologg/biobert_v1.1_pubmed')

tokenizer_bio = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=False)
model_bio = BertModel.from_pretrained('bert-base-uncased')




# Function to process text in chunks
def process_text_in_chunks(file_path, chunk_size):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_size = os.path.getsize(file_path)  # Get the total file size
        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)  # Create a tqdm progress bar

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            doc_sci_sm = nlp_sci_sm(chunk)
            diseases_sci_sm = [ent.text for ent in doc_sci_sm.ents if ent.label_ == 'DISEASE']
            drugs_sci_sm = [ent.text for ent in doc_sci_sm.ents if ent.label_ == 'DRUG']

            yield diseases_sci_sm, drugs_sci_sm

            progress_bar.update(len(chunk))  # Update the progress bar

        progress_bar.close()  # Close the progress bar

# Set a reasonable chunk size
chunk_size = 100000
results_generator = process_text_in_chunks('combined_text.txt', chunk_size)

# Process the generator results as needed
# ... (previous code remains the same)

# Process the generator results as needed
diseases_sci_sm = []
drugs_sci_sm = []
diseases_bio = []  # Add this line to define diseases_bio
drugs_bio = []  # Add this line to define drugs_bio

for diseases_chunk, drugs_chunk in results_generator:
    diseases_sci_sm.extend(diseases_chunk)
    drugs_sci_sm.extend(drugs_chunk)

    # Append the diseases and drugs for BioBERT
    diseases_bio.extend(tokenizer_bio.tokenize(tokenizer_bio.decode(tokenizer_bio.encode(' '.join(diseases_chunk)))))
    drugs_bio.extend(tokenizer_bio.tokenize(tokenizer_bio.decode(tokenizer_bio.encode(' '.join(drugs_chunk)))))

# Tokenize and process text using BioBERT
inputs_bio = tokenizer_bio(' '.join(diseases_sci_sm + drugs_sci_sm), return_tensors="pt")
outputs_bio = model_bio(**inputs_bio)

# Extract predicted tokens from the BioBERT model output
predicted_tokens_bio = tokenizer_bio.convert_ids_to_tokens(outputs_bio.last_hidden_state.argmax(dim=-1).squeeze().tolist())

# Continue with the comparison of results, printing, and analysis
common_diseases = set(diseases_sci_sm) & set(diseases_bio)
common_drugs = set(drugs_sci_sm) & set(drugs_bio)

# ... (rest of your code remains the same)


unique_diseases_sci_sm = set(diseases_sci_sm) - set(diseases_bio)
unique_drugs_sci_sm = set(drugs_sci_sm) - set(drugs_bio)

unique_diseases_bio = set(diseases_bio) - set(diseases_sci_sm)
unique_drugs_bio = set(drugs_bio) - set(drugs_sci_sm)

# Print results or perform further analysis as needed
print("Total entities detected by spaCy model:", len(diseases_sci_sm) + len(drugs_sci_sm))
print("Total entities detected by BioBERT:", len(diseases_bio) + len(drugs_bio))
print("Common diseases:", common_diseases)
print("Common drugs:", common_drugs)
print("Unique diseases (spaCy - en_core_sci_sm):", unique_diseases_sci_sm)
print("Unique drugs (spaCy - en_core_sci_sm):", unique_drugs_sci_sm)
print("Unique diseases (BioBERT):", unique_diseases_bio)
print("Unique drugs (BioBERT):", unique_drugs_bio)

# Check for the most common words in each category using Counter
common_words_diseases_sci_sm = Counter(diseases_sci_sm).most_common()
common_words_drugs_sci_sm = Counter(drugs_sci_sm).most_common()

common_words_diseases_bio = Counter(diseases_bio).most_common()
common_words_drugs_bio = Counter(drugs_bio).most_common()

# Display or further analyze the results as needed
print("Common words in diseases (spaCy - en_core_sci_sm):", common_words_diseases_sci_sm)
print("Common words in drugs (spaCy - en_core_sci_sm):", common_words_drugs_sci_sm)
print("Common words in diseases (BioBERT):", common_words_diseases_bio)
print("Common words in drugs (BioBERT):", common_words_drugs_bio)
