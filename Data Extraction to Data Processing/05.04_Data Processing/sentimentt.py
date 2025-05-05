import os
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Debug: Print current working directory to verify file location
print("Current working directory:", os.getcwd())

# Download the VADER lexicon if not already done
nltk.download('vader_lexicon')

# Use an absolute path to ensure the file is found (adjust the path as needed)
file_path = "Cleaned_stack.csv"
df = pd.read_csv(file_path, encoding="latin1")  # Use errors="ignore" if needed

# Check that the required columns exist
if 'lemmatized_text_question_body' not in df.columns:
    raise KeyError("Column 'lemmatized_text_question_body' not found. Found columns: " + str(df.columns.tolist()))
if 'lemmatized_text_accepted_answer_body' not in df.columns:
    raise KeyError("Column 'lemmatized_text_accepted_answer_body' not found. Found columns: " + str(df.columns.tolist()))

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Define a function to compute the compound sentiment score, converting input to string
def get_sentiment(text):
    text = str(text)  # Ensure text is a string
    scores = sid.polarity_scores(text)
    return scores['compound']

# Compute sentiment scores for the question and answer columns
df['sentiment_score_question'] = df['lemmatized_text_question_body'].apply(get_sentiment)
df['sentiment_score_answer'] = df['lemmatized_text_accepted_answer_body'].apply(get_sentiment)

# Display the first few rows to verify the new columns
print(df.head())

# Save the updated DataFrame to a new CSV file
output_filename = "so_with_sentiment.csv"
df.to_csv(output_filename, index=False)
print(f"Updated CSV with sentiment scores saved as '{output_filename}'")
