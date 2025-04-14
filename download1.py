import pandas as pd
import requests
import os
import time
import random

# Your CORE API Key
CORE_API_KEY = ""

# Endpoint
CORE_SEARCH_API = "https://api.core.ac.uk/v3/search/works"

# Create folder to save PDFs
PDF_DIR = "papers1"
os.makedirs(PDF_DIR, exist_ok=True)

# Search paper using CORE API
def search_core_pdf(title, retries=5):
    headers = {
        "Authorization": f"Bearer {CORE_API_KEY}"
    }

    params = {
        "q": title,
        "page": 1,
        "pageSize": 1
    }

    for attempt in range(retries):
        try:
            response = requests.get(CORE_SEARCH_API, headers=headers, params=params)
            if response.status_code == 429:
                wait = 5 * (2 ** attempt)
                print(f"🚫 CORE API rate limit – Retrying in {wait} seconds...")
                time.sleep(wait)
                continue
            response.raise_for_status()
            data = response.json()

            if "results" not in data or not data["results"]:
                return None, "not found"

            work = data["results"][0]
            pdf_url = work.get("downloadUrl")

            return pdf_url, "no pdf" if not pdf_url else "downloaded"

        except Exception as e:
            print(f"❌ Error on attempt {attempt + 1} for title '{title}': {e}")
            time.sleep(3)

    return None, "error"

# Download PDF
def download_pdf(pdf_url, filename):
    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"❌ Download failed for {filename} from {pdf_url}: {e}")
        return False

# Main function
def download_papers_from_core(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    results = []

    for idx, row in df.iterrows():
        project_id = row["id"]
        title = row["osf_title"]

        if pd.isna(title):
            results.append({"id": project_id, "osf_title": title, "status": "no title", "pdf_url": ""})
            continue

        print(f"\n🔍 [{idx + 1}/{len(df)}] Searching: {title}")
        pdf_url, status = search_core_pdf(title)

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

        sleep_time = random.uniform(3, 6)
        print(f"⏳ Sleeping for {sleep_time:.2f} seconds...\n")
        time.sleep(sleep_time)

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_csv, index=False)
    print(f"\n✅ All results saved to: {output_csv}")

if __name__ == "__main__":
    download_papers_from_core("remaining.csv", "remaining_core_downloaded.csv")