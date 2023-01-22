import fitz
from fitz import PDF_ENCRYPT_KEEP
import re

pdf = fitz.open("high.pdf")

#to count the number of pages
print("no of pages are",pdf.page_count)

#print data
a=pdf.metadata
print(a["format"])

# get table content
for i in pdf.get_toc():
    print(i[2])

l=[]
page =pdf.load_page(14)
text=page.get_text()
print(text[5])
# for i in range(len(page.get_text())):
#     l.append(i)

# print(l)
l=[]
for i in range(len(text)):
    l.append(text[i])

print(l+) 


