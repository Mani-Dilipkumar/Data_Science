
# QNX Project Overview

The **QNX Project** is a structured pipeline aimed at extracting, processing, and analyzing developer sentiment and communication metadata from technical forums and repositories such as QNX, Unreal Engine, and OpenAI-related sources. The project encompasses three main components: data extraction, data pre-processing, and analysis.

---

## Project Directory Structure

```
QNX Project/
├── Analysis Notebooks/                            # Exploratory data analysis (EDA), visualizations, and sentiment summaries
│   ├── QNX_EDA_Sentiment.ipynb                    # Jupyter notebook with QNX developer sentiment graphs, topic trends
│   └── Unreal_Insights_Analysis.ipynb             # Timeline plots, repo activity, contributor heatmaps
│
└── Data Extraction to Data Processing/
    ├── 05.04_Data Collection_with code/
    │   ├── files/                                 # Raw source data (txt, csv, json)
    │   │   ├── qnx_raw_comments.txt               # Unfiltered QNX comments
    │   │   └── unreal_forum_dump.json             # Unreal Engine discussions
    │   └── venv_code/
    │       ├── 1. Openai/                         # OpenAI prompt engineering & response parsing
    │       ├── 2. QNX/                            # QNX-focused extraction: logs → developer insights
    │       ├── 3. Unreal Engine/                  # Unreal scraping: GitHub contributors, changelogs
    │       ├── docx-template/                     # Template for Word export automation
    │       └── site-packages/                     # Virtual env packages: transformers, torch, openai, sklearn, etc.
    │
    └── 05.04_Data Pre-processing/
        ├── Raw Data/                              # Input to preprocessing pipeline
        │   └── *.txt / *.json / *.csv             # Original scraped files
        ├── Pre-Processed data/                    # Cleaned & labeled datasets
        │   ├── QNX_cleaned_output.csv             # Cleaned and tokenized QNX dataset
        │   └── Unreal_sentiment_ready.xlsx        # Ready for visualization & modeling
        ├── venv_preprocessing/
        │   └── Scripts/
        │       ├── clean_qnx_text.py              # Normalization, token removal
        │       ├── openai_sentiment_tag.py        # Calls OpenAI for zero-shot classification
        │       ├── entity_recognition.py          # (Optional) NER via HuggingFace
        │       └── merge_and_export.py            # Merge multiple sources into one dataset
        └── README_Pre_processing.md               # Step-by-step usage and setup guide
```

---

## Organization & Flow

The project is modular and follows a logical pipeline:

1. **Data Collection** (`05.04_Data Collection_with code/`):
    - Scrapes or loads raw content from forums, logs, GitHub, and APIs.
    - Organizes scripts by target source (QNX, Unreal Engine, OpenAI).
    - Maintains a Python environment (`venv_code/`) with necessary packages preinstalled.

2. **Pre-processing** (`05.04_Data Pre-processing/`):
    - Cleans raw data (removes HTML, normalizes text, drops noise).
    - Tags sentiment using OpenAI API.
    - Optionally performs named entity recognition (NER).
    - Final data stored in "Pre-Processed data" for downstream use.

3. **Analysis** (`Analysis Notebooks/`):
    - Notebooks consume cleaned datasets for exploratory analysis.
    - Visualize developer sentiment over time, trends across tech stacks, or contributor dynamics.

---

## Additional Documentation

- A focused and **detailed README** is available inside each subdirectory:
  - `README_Pre_processing.md` covers environment setup, dependencies, and script usage.
  - Scripts in each code folder include inline documentation and comments.
  - `docx-template/` provides automated export formatting for summary reports.

---

## Technologies Used

- **Python Libraries**: `pandas`, `numpy`, `transformers`, `openai`, `regex`, `scikit-learn`, `tqdm`, `matplotlib`, `docx`, `pywin32`
- **Modeling/Tagging**: OpenAI GPT, HuggingFace NER pipelines
- **Environment**: Virtualenv-based isolation for each stage (`venv_code`, `venv_preprocessing`)
- **Visualization**: Jupyter Notebooks

---

## Getting Started

1. Clone the repository and navigate to the desired directory.
2. Activate the relevant virtual environment:
   ```bash
   source venv_code/Scripts/activate
   # or
   source venv_preprocessing/Scripts/activate
   ```
3. Run scripts as documented in the appropriate README files.
4. Open the notebooks under `Analysis Notebooks/` to visualize and interpret findings.

For any questions or custom exports, refer to the usage examples and automation template in `docx-template/`.
