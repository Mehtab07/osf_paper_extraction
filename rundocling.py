from docling.document_converter import DocumentConverter

source = "test/2sz48.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

# Markdown file to save
# output_path = "paper_output.md"

# with open(output_path, "w", encoding="utf-8") as f:
#     # Title
#     if result.title:
#         f.write(f"# {result.title}\n\n")

#     # Authors
#     if result.authors:
#         authors_str = ", ".join(result.authors)
#         f.write(f"**Authors:** {authors_str}\n\n")

#     # DOI
#     if result.doi:
#         f.write(f"**DOI:** {result.doi}\n\n")

#     # Abstract
#     if result.abstract:
#         f.write("## Abstract\n\n")
#         f.write(result.abstract + "\n\n")

#     # Sections
#     if result.sections:
#         for section in result.sections:
#             if section.title:
#                 f.write(f"## {section.title}\n\n")
#             if section.text:
#                 f.write(section.text.strip() + "\n\n")