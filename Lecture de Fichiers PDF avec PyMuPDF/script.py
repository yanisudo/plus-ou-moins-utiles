import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_text = extract_text_from_pdf('path/to/your/document.pdf')
    print(pdf_text)