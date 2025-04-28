from grobid_client.grobid_client import GrobidClient
client = GrobidClient(config_path="./config.json")  # Default config

# Process a PDF
response = client.process_pdf(
    "paper.pdf", 
    service="processFulltextDocument",  # Extract full text + metadata
    generateIDs=True, 
    consolidate_header=True
)

print(response.text)  # Returns TEI/XML with structured content