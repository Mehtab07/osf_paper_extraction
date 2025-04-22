# 📝 OSF Paper Extraction

This project helps in automating the process of downloading research paper PDFs using paper titles and IDs. It supports searching via **CORE API** and **Semantic Scholar API**, and saves the PDFs locally along with their status in CSV files, and now also includes functionality to extract and summarize specific sections of research papers using OpenAI's GPT models.

---

## 📁 Project Structure
```bash
osf_paper_extraction/
│
├── cleaning/                     # Jupyter notebooks for preprocessing datasets
├── test/                         # Folder for storing test PDFs
│
├── download.py                   # Downloads PDFs via Semantic Scholar API
├── download1.py                  # Downloads PDFs via CORE API
├── apitest.py                    # Main pipeline for OpenAI-based summarization
├── rundocling.py                 # (Optional) Other experimental logic
├── output_sections.md            # Stores extracted sections in markdown format
├── testing.ipynb                 # Notebook for experiments or debugging
├── Requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Mehtab07/osf_paper_extraction.git
   cd osf_paper_extraction
   pip install -r Requirements.txt
   API_KEY = "sk-..."  #Put your own OpenAI API key here

## To Run
  ```bash
  python apitest.py
    # By default, it loads a test PDF (test/2sz48.pdf) and summarizes the "Conclusions" section.
  ```
    
## Notes  
Rate Limiting: Both APIs may enforce rate limits. The scripts implement exponential backoff and randomized sleep to reduce the chance of hitting limits.

PDF Availability: Not all titles will have a downloadable PDF. These cases are marked in the status column of the output CSV.

Folder Creation: The scripts automatically create the output folders (papers/, papers1/) if they do not exist.

Section Extraction: The section split logic currently uses common academic headers like Introduction, Method, Conclusion, etc. This can be extended as needed.