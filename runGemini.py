import os
import re
import fitz  # PyMuPDF
from google import genai
from openai import OpenAI

def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    full_text = "".join(page.get_text() for page in doc)
    doc.close()
    return full_text


def split_text_into_sections(text: str, headers=None) -> list:
    if headers is None:
        headers = [
            "Abstract", "Introduction", "Related Work", "Method", "Methods","Limitations",
            "Results", "Discussion", "Conclusion","Conclusions", "References"
        ]
    pattern = "|".join([rf"\n\s*{header}\s*\n" for header in headers])
    sections = re.split(pattern, text, flags=re.IGNORECASE)
    headers_found = re.findall(pattern, text, flags=re.IGNORECASE)
    section_dict = {header.strip(): content.strip() for header, content in zip(headers_found, sections[1:])}
    return section_dict


def save_sections_to_markdown(headers, sections, output_path="Results/script_result.md"):
    with open(output_path, "w", encoding="utf-8") as f:
        for header, content in zip(headers, sections):
            f.write(f"## {header.strip()}\n\n{content.strip()}\n\n")


def summarize_text_with_openai(text: str, api_key: str, section_to_summarize=None, max_tokens=5000) -> str:
    client = genai.Client(api_key="REMOVED_API_KEY")
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"Summarize the following text. It is from the '{section_to_summarize or 'Full Paper'}' section of a research paper. Provide a concise and non-repetitive summary:\n\n{text}")
    
    return response.text

def pipeline(pdf_path: str, api_key: str, section_to_summarize=None, output_markdown="output_sections.md"):
    # 1. Extract text
    text = extract_text_from_pdf(pdf_path)

    # 2. Split into sections
    section_dict = split_text_into_sections(text)

    # 3. Save to markdown
    save_sections_to_markdown(section_dict.keys(), section_dict.values())

    # 4. Read and summarize
    if section_to_summarize:
        section_content = section_dict.get(section_to_summarize)
        if not section_content:
            print(f" Section '{section_to_summarize}' not found.")
            return
        text_to_summarize = f"{section_to_summarize}\n\n{section_content}"
    else:
        with open("Results/script_result.md", "r", encoding="utf-8") as f:
            text_to_summarize = f.read()

    summary = summarize_text_with_openai(text_to_summarize, api_key, section_to_summarize)
    print(f"\n Summary of section: {section_to_summarize or 'Full Paper'}\n")
    print(summary)
    return summary


if __name__ == "__main__":
    PDF_PATH = "test/2sz48.pdf"
    API_KEY = os.getenv("Gemini_API_KEY")  # Replace with your OpenAI API key

    SECTION = "Results"  # Or None for full paper
    pipeline(PDF_PATH, API_KEY, section_to_summarize=SECTION)
