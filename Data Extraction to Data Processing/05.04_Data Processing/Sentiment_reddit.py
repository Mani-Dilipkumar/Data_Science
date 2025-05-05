import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if needed
nltk.download('vader_lexicon')

# Use an encoding that can handle problematic characters (e.g., 'latin1')
df = pd.read_csv("Cleaned_reddit.csv", encoding="latin1")

# Check that the expected column exists
if 'lemmatized_text' not in df.columns:
    raise KeyError(f"Column 'lemmatized_text' not found. Columns available: {df.columns.tolist()}")

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Define a function to compute sentiment that converts input to string
def get_sentiment(text):
    # Convert text to string to handle any non-string (e.g., float) entries
    text = str(text)
    scores = sid.polarity_scores(text)
    return scores['compound']

# Apply the sentiment function to the 'lemmatized_text' column
df['sentiment_score'] = df['lemmatized_text'].apply(get_sentiment)

# Display the first few rows to verify
print(df.head())

# Save the updated DataFrame to a new CSV file
output_filename = "Cleaned_reddit_with_sentiment.csv"
df.to_csv(output_filename, index=False)
print(f"Updated CSV with sentiment scores saved as '{output_filename}'")
