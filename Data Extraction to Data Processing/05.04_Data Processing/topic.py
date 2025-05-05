# Import necessary libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from gensim import corpora, models
import string

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Define stopwords list
stop_words = set(stopwords.words('english'))

# Function to preprocess text: lower-case, remove punctuation, tokenize, remove stopwords
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize by splitting on whitespace
    tokens = text.split()
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Read the Excel file (replace with actual file path if necessary)
df = pd.read_csv('Cleaned_reddit.csv')

# Assume the relevant text column is named 'lemmatized_text'
# and the sentiment score column is named 'sentiment_score'
# Adjust column names if they differ in your file
if 'lemmatized_text' not in df.columns or 'sentiment_score' not in df.columns:
    raise ValueError("Required columns ('lemmatized_text', 'sentiment_score') not found in the dataset.")

# Split the dataset into two subsets based on sentiment score condition:
# One subset for sentiment scores less than 0 and one for scores greater than 0.
df_negative = df[df['sentiment_score'] < 0]
df_positive = df[df['sentiment_score'] > 0]

# Preprocess the text data for each subset.
# Create a list of token lists for each document.
documents_negative = df_negative['lemmatized_text'].dropna().astype(str).apply(preprocess_text).tolist()
documents_positive = df_positive['lemmatized_text'].dropna().astype(str).apply(preprocess_text).tolist()

# Create a dictionary and corpus for each subset using Gensim
dictionary_negative = corpora.Dictionary(documents_negative)
corpus_negative = [dictionary_negative.doc2bow(doc) for doc in documents_negative]

dictionary_positive = corpora.Dictionary(documents_positive)
corpus_positive = [dictionary_positive.doc2bow(doc) for doc in documents_positive]

# Set parameters for LDA; you can adjust num_topics as desired
num_topics = 5
passes = 10

# Perform LDA topic modelling for the negative sentiment subset
lda_model_negative = models.LdaModel(corpus=corpus_negative,
                                     id2word=dictionary_negative,
                                     num_topics=num_topics,
                                     random_state=42,
                                     passes=passes)

# Perform LDA topic modelling for the positive sentiment subset
lda_model_positive = models.LdaModel(corpus=corpus_positive,
                                     id2word=dictionary_positive,
                                     num_topics=num_topics,
                                     random_state=42,
                                     passes=passes)

# Print the topics for the negative sentiment subset
print("LDA Topics for Negative Sentiment (sentiment_score < 0):")
for idx, topic in lda_model_negative.print_topics(num_topics=num_topics, num_words=10):
    print("Topic {}: {}".format(idx, topic))

print("\n" + "="*80 + "\n")

# Print the topics for the positive sentiment subset
print("LDA Topics for Positive Sentiment (sentiment_score > 0):")
for idx, topic in lda_model_positive.print_topics(num_topics=num_topics, num_words=10):
    print("Topic {}: {}".format(idx, topic))
