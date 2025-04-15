import pandas as pd
import requests
import time
import random

# Generic function to handle retries with exponential backoff
def make_request_with_retry(url, max_retries=5, base_delay=1):
    for attempt in range(max_retries):
        response = requests.get(url)
        if response.status_code == 429:
            wait_time = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Rate limited (429). Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
        else:
            response.raise_for_status()
            return response
    raise Exception("Max retries exceeded due to rate limiting.")

def get_osf_title(project_id):
    url = f"https://api.osf.io/v2/nodes/{project_id}/"
    try:
        response = make_request_with_retry(url)
        title = response.json().get("data", {}).get("attributes", {}).get("title", None)
        print(f"Fetched title for {project_id}: {title}")
        return title
    except Exception as e:
        print(f"Error fetching title for {project_id}: {e}")
        return None

def get_contributors(project_id):
    url = f"https://api.osf.io/v2/nodes/{project_id}/contributors/?embed=users"
    contributors = []
    
    try:
        while url:
            response = make_request_with_retry(url)
            data = response.json()
            
            for contrib in data.get("data", []):
                user_data = contrib.get("embeds", {}).get("users", {}).get("data", {})
                full_name = user_data.get("attributes", {}).get("full_name", "Unknown")
                contributors.append(full_name)
            
            url = data.get("links", {}).get("next", None)
            if url:
                time.sleep(1)  # Delay before fetching next page
        
        print(f"Found {len(contributors)} contributors for {project_id}")
        return contributors if contributors else ["No contributors found"]
        
    except Exception as e:
        print(f"Error fetching contributors for {project_id}: {e}")
        return ["Error fetching contributors"]

def add_titles_and_contributors_to_csv(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)

    if "id" not in df.columns:
        raise ValueError("CSV must contain an 'id' column.")

    df["osf_title"] = df["id"].apply(lambda pid: get_osf_title(str(pid)))
    df["contributors"] = df["id"].apply(lambda pid: get_contributors(str(pid)))

    df.to_csv(output_csv_path, index=False)
    print(f"Saved updated CSV to {output_csv_path}")

if __name__ == "__main__":
    input_csv = "project_ids.csv"
    output_csv = "Id_Title_Contributors.csv"
    add_titles_and_contributors_to_csv(input_csv, output_csv)
