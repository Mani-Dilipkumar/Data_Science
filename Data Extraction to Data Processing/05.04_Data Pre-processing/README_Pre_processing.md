# Pre-Processing Pipeline

This repository contains a data preprocessing pipeline for Reddit comment data, including cleaning, tokenization, sentiment analysis, and feature engineering.

## Project Structure

```
project-root/
├── venv/                             # Python virtual environment
│   ├── etc/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   └── ...                          # other venv files and folders
├── multiple_reddit_posts_comments8.csv  # Raw input data
├── Pre_Processing.ipynb                # Jupyter notebook with preprocessing steps
├── Pre_Processed.xlsx                  # Processed data output (version 1)
├── Pre_Processed2.xlsx                 # Processed data output (version 2)
└── .gitignore                          # Files to ignore in version control
```

## Requirements

- Python 3.8 or higher
- Install dependencies:

```bash
pip install pandas numpy nltk matplotlib openpyxl
```

## Pipeline Steps

1. Load Data 
   Read the raw CSV file `multiple_reddit_posts_comments8.csv` into a DataFrame.

2. Data Cleaning
   - Drop rows with missing `comment_body`.  
   - Remove duplicate entries.  
   - Convert timestamp column to datetime.

3. Text Cleaning
   - Convert text to lowercase.  
   - Remove URLs, user mentions, and non-alphanumeric characters.  
   - Strip extra whitespace.

4. Tokenization & Stopword Removal
   - Download and load NLTK stopwords.  
   - Tokenize cleaned text and filter out stopwords.

5. Sentiment Analysis   (Only for Reddit)
   - Download and load VADER lexicon.  
   - Compute sentiment scores (compound, positive, negative, neutral).

6. Feature Engineering  
   - Extract date or other time-based features.  
   - Flag extreme sentiment values based on custom thresholds.

7. Visualization 
   - Plot sentiment distribution histograms.  
   - Plot time series of average sentiment over time.

8. Save Outputs  
   - Export the cleaned and augmented DataFrame to `Pre_Processed.xlsx` and `Pre_Processed2.xlsx`.

## Usage

Open `Pre_Processing.ipynb` in Jupyter and run cells in order. Alternatively, convert the notebook to a script:

```bash
jupyter nbconvert --to script Pre_Processing.ipynb
python Pre_Processing.py
```

## Notes

- Ensure NLTK resources are downloaded within the environment:

  ```python
  import nltk
  nltk.download('stopwords')
  nltk.download('vader_lexicon')
  nltk.download('punkt')
  ```
  
- Use an Excel viewer or pandas to inspect the `.xlsx` output files.
