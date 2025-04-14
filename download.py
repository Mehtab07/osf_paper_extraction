import pandas as pd
import requests
import os
import time
import random

PDF_DIR = "papers"
os.makedirs(PDF_DIR, exist_ok=True)

SEARCH_API = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_paper_pdf(title, retries=5):
    params = {
        "query": title,
        "fields": "title,openAccessPdf,url",
        "limit": 1
    }

    for attempt in range(retries):
        try:
            response = requests.get(SEARCH_API, params=params)
            if response.status_code == 429:
                wait = 5 * (2 ** attempt) 
                print(f" Rate limited (429). Retrying in {wait} seconds...")
                time.sleep(wait)
                continue  
            response.raise_for_status()
            data = response.json()

            if data["total"] == 0 or not data["data"]:
                return None, "not found"

            paper = data["data"][0]
            pdf_link = paper.get("openAccessPdf", {}).get("url")
            return pdf_link, "no pdf" if pdf_link is None else "downloaded"

        except requests.RequestException as e:
            print(f" Error on attempt {attempt+1} for '{title}': {e}")
            time.sleep(3)
    
    return None, "error"

def download_pdf(pdf_url, filename):
    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return True
    except Exception as e:
        print(f" Download failed for {filename} from {pdf_url}: {e}")
        return False

def process_titles(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    results = []

    for idx, row in df.iterrows():
        project_id = row["id"]
        title = row["osf_title"]

        if pd.isna(title):
            results.append({"id": project_id, "osf_title": title, "status": "no title", "pdf_url": ""})
            continue

        print(f"\n🔍 [{idx+1}/{len(df)}] Searching: {title}")
        pdf_url, status = search_paper_pdf(title)

        if status == "downloaded" and pdf_url:
            filename = os.path.join(PDF_DIR, f"{project_id}.pdf")
            success = download_pdf(pdf_url, filename)
            status = "downloaded" if success else "download error"

        results.append({
            "id": project_id,
            "osf_title": title,
            "status": status,
            "pdf_url": pdf_url or ""
        })

        sleep_time = random.uniform(4, 8)
        print(f" Sleeping for {sleep_time:.2f} seconds...\n")
        time.sleep(sleep_time)

    # Save results
    result_df = pd.DataFrame(results)
    result_df.to_csv(output_csv, index=False)
    print(f"\n All results saved to: {output_csv}")

if __name__ == "__main__":
    input_csv = "my_id_with_titles.csv"
    output_csv = "semantic_search_results.csv"
    process_titles(input_csv, output_csv)
