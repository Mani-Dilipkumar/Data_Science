# Developer Ecosystem Data Collection Project

This project extracts and analyzes Reddit and Stack Overflow content related to specific technology ecosystems: OpenAI, QNX, and Unreal Engine. Each platform has a dedicated folder inside `data_collection/`, following a consistent data pipeline.

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Project Structure

```
project-root/
│
├── README.md
├── requirements.txt
│
├── data_collection/
│   ├── openai/
│   │   ├── 1_extract_urls.py
│   │   ├── 2_format_urls.py
│   │   ├── 3_fetch_reddit_posts.py
│   │   ├── 4_fetch_stackoverflow_comments.py
│   │   ├── keywords.txt
│   │   ├── openai_results.xlsx
│   │   └── openai_urls.docx
│   │
│   ├── qnx/
│   │   ├── 1_extract_urls.py
│   │   ├── 2_format_urls.py
│   │   ├── 3_fetch_reddit_posts.py
│   │   ├── 4_fetch_stackoverflow_comments.py
│   │   ├── keywords.txt
│   │   ├── qnx_results.xlsx
│   │   └── qnx_urls.docx
│   │
│   └── unreal/
│       ├── 1_extract_urls.py
│       ├── 2_format_urls.py
│       ├── 3_fetch_reddit_posts.py
│       ├── 4_fetch_stackoverflow_comments.py
│       ├── keywords.txt
│       ├── unreal_results.xlsx
│       └── unreal_urls.docx
│
└── utils/
    └── common_functions.py  # reusable functions (e.g., URL cleaning, Reddit API calls)
```

## How It Works

Each platform folder contains:

- `1_extract_urls.py`: Searches Reddit and Stack Overflow using keywords.
- `2_format_urls.py`: Cleans and formats the collected URLs.
- `3_fetch_reddit_posts.py`: Downloads post content from Reddit.
- `4_fetch_stackoverflow_comments.py`: Retrieves Q&A threads from Stack Overflow.
- `keywords.txt`: Contains search terms related to the platform.
- `*_results.xlsx`: Final output of the collected and cleaned data.
- `*_urls.docx`: A formatted document with all extracted URLs for reference.

## Usage Example

```bash
cd data_collection/openai
python 1_extract_urls.py
python 2_format_urls.py
python 3_fetch_reddit_posts.py
python 4_fetch_stackoverflow_comments.py
# Repeat similarly for qnx and unreal folders.
```

## Reusability

The `utils/common_functions.py` file contains shared code such as:

- API wrappers
- URL parsing and validation
- File export helpers

These can be imported into individual scripts to reduce duplication.

## Notes

- Reddit access may require API credentials via PRAW or similar libraries.
- Stack Overflow extraction should respect StackExchange API terms.
- Outputs are designed for analysis and reporting in `.xlsx` and `.docx` formats.
