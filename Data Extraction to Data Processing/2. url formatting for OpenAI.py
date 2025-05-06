from docx import Document

def extract_urls_from_docx(file_path: str):
    doc = Document("openai.docx")
    urls = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if text.startswith("http") and "reddit.com" in text:
            urls.append(text)
    
    return urls

# Example usage
file_path = 'openai'
urls = extract_urls_from_docx(file_path)
print("urls = [")
for url in urls:
    print(f'    "{url}",')
print("]")
