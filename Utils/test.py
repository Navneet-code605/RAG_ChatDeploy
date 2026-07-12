from pdf_loader import load_pdf
text = load_pdf("medsample.pdf")
print("Length of extracted text:", len(text))
print("Preview:\n", text[:500])
