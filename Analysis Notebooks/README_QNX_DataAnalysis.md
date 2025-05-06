# Developer Engagement in QNX – Data Analysis

This repository contains the code notebooks used to extract, filter, and analyze developer sentiment and engagement data across QNX and comparable ecosystems like Unreal Engine and OpenAI. The analysis supports the findings in the final report titled "Revised_Manimalavan_Dilipkumar_MABA_W2025_Developer_Engagement_in_QNX.pdf".

## Contents

### r_DataAnalysis_Part 1.ipynb
Focus: Initial data cleaning and platform segmentation  
- Filters raw CSV exports from online forums (e.g., Reddit, Stack Overflow).
- Isolates posts mentioning QNX, Unreal Engine, or OpenAI using keyword-based filters.
- Begins thematic structuring by introducing columns like `Platform`, `Theme`, and `Category`.
- Relevant Sections:  
  - Performance: Discussions about system performance and reliability  
  - Activity: User post frequency and community involvement  
  - Efficiency: Toolchain and debugging support

### r_DataAnalysis_Part 2.ipynb
Focus: Keyword scoring and sentiment tagging  
- Applies rule-based filters and scores to classify post themes (setup issues, API problems, etc.).
- Uses basic NLP techniques to tag sentiment (positive, neutral, negative).
- Compares thematic strength across platforms (e.g., more complaints about debugging in QNX).
- Relevant Sections:  
  - Continues from Part 1 with deeper scoring logic under the same headings

### r_DataAnalysis_Part 3.ipynb
Focus: Export and final clean-up  
- Final dataset preparation for graph generation and summary tables
- Removes outliers and normalizes scores for visual presentation in the PDF report

## Relevance to Report

These notebooks form the quantitative foundation of your comparative study. They provide:
- Structured evidence of developer engagement differences
- Sentiment trends over time
- Topic frequencies for pain-point identification
- Reproducible scripts for further research or academic extension

## How to Use

1. Place your raw CSV files of forum data in the root directory.
2. Run each notebook in order (Part 1 → Part 2 → Part 3).
3. Final outputs (processed CSVs and charts) will be ready for presentation or visualization.
