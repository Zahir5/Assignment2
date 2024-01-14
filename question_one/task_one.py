import pandas as pd

# List of CSV files
csv_files = ['CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Output text file
output_file = 'combined_text.txt'

# Initialize an empty list to store 'TEXT' columns
text_columns = []

# Loop through each CSV file
for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Extract the 'TEXT' column and append it to the list
    text_columns.append(df['TEXT'])

# Concatenate all 'TEXT' columns into a single series
combined_text = pd.concat(text_columns, ignore_index=True)

# Write the combined 'TEXT' series to a text file
combined_text.to_csv(output_file, index=False, header=False)

print(f"Combined 'TEXT' columns written to {output_file}")


# requirements.txt file will server as task two (libraries installed properly)
