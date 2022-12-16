import fitz
import io
from PIL import Image

file = "static/book1.pdf"

pdf = fitz.open(file)
 
# print(pdf.page_count)
# print(pdf.metadata)
#get index
#print("toc",pdf.get_toc())
#print(pdf.load_page(1))

page = pdf.load_page(1)  # loads page number 'pno' of the document (0-based)
pix = page.get_pixmap()
pix.save("static/ikigai-page-%i.jpeg" % page.number)
print("success")