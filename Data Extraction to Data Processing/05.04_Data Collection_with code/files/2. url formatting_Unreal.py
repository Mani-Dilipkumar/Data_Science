from docx import Document

def extract_urls_from_docx(file_path: str):
    doc = Document("unreal_urls.docx")
    urls = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if text.startswith("http") and "reddit.com" in text:
            urls.append(text)
    
    return urls

# Example usage
file_path = 'qnx_urls2.docx'
urls = extract_urls_from_docx(file_path)
print("urls = [")
for url in urls:
    print(f'    "{url}",')
print("]")
