# 📝 OSF Paper Extraction and Result Comparison

This project helps in automating the process of downloading research paper PDFs using paper titles and IDs. It supports searching via **Semantic Scholar API**, and saves the PDFs locally along with their status in CSV files, and now 
## Research Paper Analysis

This tool also includes functionality to extract and summarize specific sections of research papers and compares research paper PDFs with R script execution logs using either OpenAI or Gemini AI models.


---

## 📁 Project Structure
```bash
osf_paper_extraction/
│
├── notebooks/                    # Jupyter notebooks for preprocessing datasets
├── semantic-papers/              # Research papers downloaded from Semantic-Scholar
├── papers1/                      # Research papers downloaded from Core-API and other resources
├── csv_files/                    # CSVs contaiing metadata and project IDs with status.
├── test/                         # Folder for storing test PDFs
│
├── download_semantic_papers.py   # Downloads PDFs via Semantic Scholar API
├── download1.py                  # Downloads PDFs via CORE API
├── run_openai.py                 # Main pipeline for OpenAI-based summarization and Rscript result comparison
├── run_gemini.py                 # Pipeline for gemini-based pdf and Rscript result comparison
├── runai_ml.py                   # Pipelines for summarization using other free API resources.
├── markdown_docling.py           # (Optional) Pdf to markdown conversion.
├── results                       # Stores extracted sections in markdown format
├── report.ipynb                  # Notebook for documentation of findings in the process.
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Mehtab07/osf_paper_extraction.git
   cd osf_paper_extraction
   Create a `.env` file in the root directory with your API keys:
   pip install -r requirements.txt

## To Run
  ```bash
  OpenAI Version (`run_openai.py`)
  # Processes PDF by converting to markdown first, then compares with log file. By default, it loads a test PDF (test/7h94n.pdf) and its Rscript result from 7h94n_execution.log, it can be edited to any section or full paper
  ```
  ```bash
  Gemini Version (`run_gemini.py`)
  # It takes PDF directly, then compares with log file. By default, it loads a test PDF (test/7h94n.pdf) and its Rscript result from 7h94n_execution.log.
  ```
## Notes  
Rate Limiting: Both APIs while downloading Research Papers may enforce rate limits. The scripts implement exponential backoff and randomized sleep to reduce the chance of hitting limits.

PDF Availability: Not all titles will have a downloadable PDF. These cases are marked in the status column of the output CSV.

Folder Creation: The scripts automatically create the output folders (papers/, papers1/) if they do not exist.

Section Extraction: The section split logic currently uses common academic headers like Introduction, Method, Conclusion, etc. This can be extended as needed.