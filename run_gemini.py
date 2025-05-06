import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def extract_log_file(log_path: str) -> str:
    with open(log_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def compare_pdf_and_log_with_gemini(pdf_path: str, log_path: str, api_key: str, section_to_summarize: str = None) -> str:
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Initialize the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Upload both files
    pdf_file = genai.upload_file(pdf_path, mime_type="application/pdf")
    log_file = genai.upload_file(log_path, mime_type="text/plain") 

    # Prepare the comparison prompt
    prompt = """
    You are a research analysis AI. Compare the R script execution results (from the log file) 
    with the results reported in the research paper (PDF). Specifically analyze:

    1. Numerical results - identify any mismatches between calculated and reported values
    2. Missing results - check if any computed results are missing from the paper or vice versa
    3. Methodological consistency - verify if methods described match the implementation
    4. Statistical significance - note any discrepancies in reported significance

    Provide a detailed comparison with specific examples where they exist.
    """

    # Generate the comparison
    response = model.generate_content([prompt, pdf_file, log_file])

    return response.text

if __name__ == "__main__":
    PDF_PATH = "test/7h94n.pdf"
    LOG_PATH = "test/7h94n_execution.log"
    API_KEY = os.getenv("Gemini_API_KEY")

    # Generate output filename based on input PDF
    pdf_code = os.path.splitext(os.path.basename(PDF_PATH))[0]
    OUTPUT_TXT = f"{pdf_code}_comparison_gemini.txt"

    # Run comparison
    comparison = compare_pdf_and_log_with_gemini(PDF_PATH, LOG_PATH, API_KEY)

    # Save results
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write(comparison)
    
    print(f"\nComparison saved to {OUTPUT_TXT}")
    print(comparison)