import fitz
from fitz import PDF_ENCRYPT_KEEP

pdf = fitz.open("high.pdf")

#to count the number of pages
print("no of pages are",pdf.page_count)

#print data
a=pdf.metadata
print(a["format"])
