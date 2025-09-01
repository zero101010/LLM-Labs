import pymupdf # imports the pymupdf library
import time # imports the time library for measuring execution time


PDF_PATH = "./container.pdf" # path to the PDF file


def extract_text_with_pymupdf(file_path):
    """Extracts text from a PDF using PyMuPDF."""
    full_text = ""
    start_time_pymupdf = time.time()
    try:
        doc = pymupdf.open(file_path) # open a document
        for page in doc: # iterate the document pages
          full_text += page.get_text()
        doc.close()
    except Exception as e:
        full_text = f"An error occurred: {e}"
    end_time_pymupdf = time.time()
    return full_text, end_time_pymupdf - start_time_pymupdf

from pypdf import PdfReader

def extract_text_with_pypdf(file_path):
    """Extracts text from a PDF using pypdf."""
    full_text = ""
    start_time = time.time()
    try:
        reader = PdfReader(file_path)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            full_text += page.extract_text()
    except Exception as e:
        full_text = f"An error occurred: {e}"
    end_time = time.time()
    return full_text, end_time - start_time



print(f"--- pypdf (PdfReader) ---")
pypdf_text, pypdf_time = extract_text_with_pypdf(PDF_PATH)
print(f"Time taken with pypdf: {pypdf_time:.2f} seconds")
print("-" * 20)
print(f"--- PyMuPDF ---")
pymupdf_text, pymupdf_time = extract_text_with_pymupdf(PDF_PATH)
print(f"Time taken with PyMuPDF: {pymupdf_time:.2f} seconds")
print("-" * 20)

print("\n--- Comparison ---")
print(f"PyMuPDF extracted {len(pymupdf_text)} characters.")
print(f"pypdf extracted {len(pypdf_text)} characters.")

if pymupdf_text == pypdf_text:
    print("The extracted text from PyMuPDF and pypdf is identical.")
else:
    print("The extracted text from PyMuPDF and pypdf is NOT identical.")
    if len(pymupdf_text) > len(pypdf_text):
        print("PyMuPDF extracted more characters.")
    elif len(pypdf_text) > len(pymupdf_text):
        print("pypdf extracted more characters.")
    else:
        print("Both extracted the same number of characters, but content differs.")

# You can add more detailed comparison here if needed, e.g., diffing the texts.

# Write extracted text to files
with open("pypdf_extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(pypdf_text)
print("\nText extracted by pypdf saved to pypdf_extracted_text.txt")

with open("pymupdf_extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(pymupdf_text)
print("Text extracted by PyMuPDF saved to pymupdf_extracted_text.txt")


 
