import fitz
from pathlib import Path
from statistics import mean
from pdf_path import pdf_source
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):
    
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        return (f"PDF file not found: {pdf_path}")

    document = fitz.open(pdf_path)
    pages = []

    for page_number in range(document.page_count):
        page = document.load_page(page_number)
        text = page.get_text()

        pages.append(
            {
                "page": page_number + 1,
                "text": text
            }
        )

    document.close()

    return pages


pages = load_pdf(pdf_source)


char_counts = []

for page in pages:
    chars = len(page["text"])
    char_counts.append(chars)

mean_chars = int(mean(char_counts))




def split_text(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = []

    for page in pages:
        split_chunks = splitter.split_text(page["text"])

        for chunk in split_chunks:
            chunks.append(
                {
                    "page": page["page"],
                    "text": chunk
                }
            )

    return chunks


chunks = split_text(pages)