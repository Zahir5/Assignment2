import pandas as pd
from collections import Counter
from transformers import AutoTokenizer
from tqdm import tqdm
import re



def top_30_words_count():
    # Initialize a Counter
    word_counts = Counter()

    # Read the combined_text.txt file line by line
    with open('combined_text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # Preprocess the line
            processed_line = re.sub(r'[^a-zA-Z\s]', '', line.lower())
            # Tokenize the line
            words = processed_line.split()
            # Update the word counts
            word_counts.update(words)

    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)

    # Display the top 30 words and their counts
    for word, count in top_30_words:
        print(f'{word}: {count}')

    # Convert the top 30 words and counts to a DataFrame
    top_30_df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])

    # Save the DataFrame to a CSV file
    top_30_df.to_csv('top_30_words.csv', index=False)

    print("Top 30 words and counts saved to 'top_30_words.csv'")



# Call the top_30_words_count() function to get the occurrence of most common 30 words
# top_30_words_count()





# The following function is being used to count top 30 tokens from the generated text file
def count_top_tokens(file_path, model_name="bert-base-uncased", top_n=30, chunk_size=512):
    # Load AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize Counter for token counts
    token_counts = Counter()

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire text
        full_text = file.read()

    # Iterate over the text in chunks
    for i in tqdm(range(0, len(full_text), chunk_size), desc="Processing chunks"):
        # Truncate the sequence to the specified chunk
        text_chunk = full_text[i:i + chunk_size]

        # Tokenize the chunk
        tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text_chunk)))

        # Update token counts
        token_counts.update(tokens)

    # Get the top N most common tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens


file_path = 'combined_text.txt'
# top_30_tokens = count_top_tokens(file_path, model_name="bert-base-uncased", top_n=30)

# # Display the top 30 tokens and their counts
# for token, count in top_30_tokens:
#     print(f'{token}: {count}')


# requirements.txt file will server as task two(all required libraries installed for NLP)



