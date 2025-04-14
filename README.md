# 📝 OSF Paper Extraction

This project helps in automating the process of downloading research paper PDFs using paper titles and IDs. It supports searching via **CORE API** and **Semantic Scholar API**, and saves the PDFs locally along with their status in CSV files.

---

## 📁 Project Structure

- **cleaning/**  
  Contains Jupyter notebooks used to preprocess and clean raw datasets before searching for papers. This may include cleaning title data, handling missing values, and generating initial CSV files like `my_id_with_titles.csv` or `remaining.csv`.

- **download.py**  
  Downloads PDFs using the **Semantic Scholar API**. It reads a CSV of paper titles and IDs, attempts to fetch the corresponding PDF URL from Semantic Scholar, and downloads it if available. The results are saved in `semantic_search_results.csv`.

- **download1.py**  
  Downloads PDFs using the **CORE API**. It functions similarly to `download.py`, but uses the authenticated CORE API, and stores downloaded PDFs in a separate folder. The results are saved in `remaining_core_downloaded.csv`.

- **requirements.txt**  
  Contains Python dependencies needed to run this project.

---

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Mehtab07/osf_paper_extraction.git
   cd osf_paper_extraction


**Notes**  
Rate Limiting: Both APIs may enforce rate limits. The scripts implement exponential backoff and randomized sleep to reduce the chance of hitting limits.

PDF Availability: Not all titles will have a downloadable PDF. These cases are marked in the status column of the output CSV.

Folder Creation: The scripts automatically create the output folders (papers/, papers1/) if they do not exist.