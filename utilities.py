import pandas as pd
def is_arabic(text):
    arabic_count = sum('\u0600' <= char <= '\u06FF' for char in text)
    english_count = sum('A' <= char <= 'Z' or 'a' <= char <= 'z' for char in text)
    return arabic_count > english_count

# Read names and check their language
def load_data(path):
    df = pd.read_csv(path)
    return df.to_dict('records')  # Convert DataFrame to a list of dictionaries




# Load the second CSV file into a list for search
