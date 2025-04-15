import pandas as pd
import requests
import time

def get_osf_title(project_id):
    url = f"https://api.osf.io/v2/nodes/{project_id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        title = response.json().get("data", {}).get("attributes", {}).get("title", None)
        print(f" Fetched title for {project_id}: {title}")
        return title
    except Exception as e:
        print(f"Error fetching title for {project_id}: {e}")
        return None

def get_contributors(project_id):
    url = f"https://api.osf.io/v2/nodes/{project_id}/contributors/?embed=users"
    contributors = []
    
    try:
        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Extract contributor names from embedded user data
            for contrib in data.get("data", []):
                user_data = contrib.get("embeds", {}).get("users", {}).get("data", {})
                full_name = user_data.get("attributes", {}).get("full_name", "Unknown")
                contributors.append(full_name)
            
            # Check for next page
            url = data.get("links", {}).get("next", None)
            if url:
                time.sleep(1)
            
        print(f"Found {len(contributors)} contributors for {project_id}")
        return contributors if contributors else ["No contributors found"]
        
    except Exception as e:
        print(f"Error fetching contributors for {project_id}: {e}")
        return ["Error fetching contributors"]

def add_titles_and_contributors_to_csv(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)

    if "id" not in df.columns:
        raise ValueError("CSV must contain a 'id' column.")

    df["osf_title"] = df["id"].apply(lambda pid: get_osf_title(str(pid)))
    df["contributors"] = df["id"].apply(lambda pid: get_contributors(str(pid)))

    df.to_csv(output_csv_path, index=False)
    print(f" Saved updated CSV to {output_csv_path}")

if __name__ == "__main__":
    input_csv = "project_ids.csv"
    output_csv = "Id_Title_Contributors.csv"
    add_titles_and_contributors_to_csv(input_csv, output_csv)