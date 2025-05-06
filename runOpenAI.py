import os
import re
import fitz  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    full_text = "".join(page.get_text() for page in doc)
    doc.close()
    return full_text

def split_text_into_sections(text: str, headers=None) -> list:
    if headers is None:
        headers = [
            "Abstract", "Introduction", "Related Work","Methodology", "Method", "Methods", "Limitations",
            "Results", "Discussion", "Conclusion", "Conclusions", "References","REFERENCES AND NOTES"
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

def extract_log_file(log_path: str) -> str:
    with open(log_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def summarize_text_with_openai(text: str, api_key: str, section_to_summarize=None, model="gpt-4.1", max_tokens=5000) -> str:
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": " You are a state-of-the-art, research-oriented AI model. Your task is to analyze this paper using the most rigorous, methodologically sound, and evidence-based review process possible, adhering to the highest standards of peer-reviewed academic scrutiny."},
            {"role": "user", "content": text}
        ],
        temperature=0.8,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def pipeline(pdf_path: str, api_key: str,output_txt, section_to_summarize=None, output_markdown="output_sections.md", log_path=None, ):
    # 1. Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # 2. Split into sections
    section_dict = split_text_into_sections(text)

    # 3. Save to markdown
    save_sections_to_markdown(section_dict.keys(), section_dict.values())

    # 4. Prepare content to summarize
    if section_to_summarize:
        section_content = section_dict.get(section_to_summarize)
        if not section_content:
            print(f" Section '{section_to_summarize}' not found.")
            return
        text_to_summarize = f"{section_to_summarize}\n\n{section_content}"
    else:
        with open("Results/script_result.md", "r", encoding="utf-8") as f:
            text_to_summarize = f.read()

    # 5. Append log content if available
    if log_path:
        log_content = extract_log_file(log_path)
        text_to_summarize = (
            "The following is a summary of code execution results from R scripts used in the research paper. "
            "After that, you'll find the text from the paper's results section. Compare both and highlight:\n\n"
            "1. Any mismatches between results reported and those computed.\n"
            "2. Any missing results in either side.\n"
            "3. Overall consistency and possible explanations if mismatches exist.\n\n"
            "--- Begin R Script Results Summary ---\n"
            f"{log_content}\n"
            "--- End Summary ---\n\n"
            "--- Begin Research Paper Text ---\n"
            f"{text_to_summarize}\n"
            "--- End Paper Text ---"
        )

    # 6. Summarize
    summary = summarize_text_with_openai(text_to_summarize, api_key, section_to_summarize)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(f"Summary of comparison between R Script Results and Research Paper Results:\n\n")
        f.write(summary)
    
    print(f"\nSummary saved to {output_txt}")
    return summary

if __name__ == "__main__":
    PDF_PATH = "test/7h94n.pdf"
    LOG_PATH = "test/7h94n_execution.log"
    API_KEY = os.getenv('OpenAI_API_KEY')

    SECTION = ""  # Leave empty or set section name like "Results"
    pdf_code = os.path.splitext(os.path.basename(PDF_PATH))[0]
    OUTPUT_TXT = f"{pdf_code}_comparison_OpenAI.txt"
    pipeline(PDF_PATH, API_KEY, section_to_summarize=SECTION, log_path=LOG_PATH, output_txt=OUTPUT_TXT)
