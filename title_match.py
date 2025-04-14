import os
import pandas as pd
import fitz  # PyMuPDF
from rapidfuzz import fuzz, process

def extract_title_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            first_page = doc[0]
            text = first_page.get_text()
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            return lines[:3]  # First 3 non-empty lines (title is likely one of them)
    except Exception as e:
        print(f"❌ Error reading {pdf_path}: {e}")
        return []

def clean_text(text):
    import re
    return re.sub(r'\W+', ' ', text).strip().lower()

def match_titles(osf_title, extracted_lines):
    osf_title_clean = clean_text(osf_title)
    scores = [(line, fuzz.token_set_ratio(osf_title_clean, clean_text(line))) for line in extracted_lines]
    best_line, best_score = max(scores, key=lambda x: x[1]) if scores else ("", 0)
    return best_line, best_score

def verify_titles(csv_file, pdf_folder, output_csv):
    df = pd.read_csv(csv_file)
    results = []

    for idx, row in df.iterrows():
        paper_id = row['id']
        osf_title = row['osf_title']
        pdf_path = os.path.join(pdf_folder, f"{paper_id}.pdf")

        if not os.path.exists(pdf_path):
            results.append({**row, "match_score": 0, "matched_line": "", "match_status": "not downloaded"})
            continue

        extracted_lines = extract_title_from_pdf(pdf_path)
        matched_line, score = match_titles(osf_title, extracted_lines)
        status = "match" if score >= 85 else "mismatch"

        results.append({
            **row,
            "matched_line": matched_line,
            "match_score": score,
            "match_status": status
        })

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_csv, index=False)
    print(f"\n✅ Title match report saved to: {output_csv}")

if __name__ == "__main__":
    verify_titles(
        csv_file="semantic_search_results.csv",
        pdf_folder="papers",
        output_csv="pdf_title_verification.csv"
    )
