import os
from PyPDF2 import PdfReader

# Path to your PDF
pdf_path = os.path.join("Data", "meddata.pdf")

# Output folder
output_folder = "Data"

def extract_chapter(start_page, end_page, output_filename):
    reader = PdfReader(pdf_path)
    text = ""

    # Loop through selected pages
    for page_num in range(start_page - 1, end_page):  # PyPDF2 is 0-indexed
        page = reader.pages[page_num]
        text += page.extract_text() + "\n"

    # Save to file
    output_path = os.path.join(output_folder, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Saved {output_filename}")

# Example usage: adjust page ranges based on Mahajan & Gupta chapters
extract_chapter(1, 27, "Epidemiology.txt")
extract_chapter(434, 449, "Biostatistics.txt")
extract_chapter(476, 523 , "Health_Programmes.txt")
extract_chapter(576, 604, "Maternal_Child_Health.txt")
extract_chapter(388, 433, "Nutrition.txt")
extract_chapter(126, 137, "Social_Environment.txt")
extract_chapter(605, 632, "Family_planning.txt")
