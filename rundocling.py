from docling.document_converter import DocumentConverter

source = "test/7h94n.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
markdown_content = result.document.export_to_markdown()

with open("results/docling.md","w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Markdown content saved to docling.md")  