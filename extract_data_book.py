# import fitz
# from fitz import PDF_ENCRYPT_KEEP
# import re

# pdf = fitz.open("high.pdf")

# #to count the number of pages
# print("no of pages are",pdf.page_count)

# #print data
# a=pdf.metadata
# print(a["format"])

# # get table content
# for i in pdf.get_toc():
#     print(i[2])

# l=[]
# page =pdf.load_page(14)
# text=page.get_text()
# print(text[5])
# # for i in range(len(page.get_text())):
# #     l.append(i)

# # print(l)


# # print("------>>>>",pdf.get_toc())

# # def book(pdf):
# #     chap=[]
# #     for i in range(len(pdf.get_toc())):
# #         chap.append(pdf.get_toc()[i])
# #     for i in range(chap.__len__()):
# #         print(chap[i])

# # book(pdf)

# print(pdf.get_toc()[6])
from PyPDF2 import PdfReader
pdf="D:/telegram/Telegram Desktop/mf/storytelling-with-data-cole-nussbaumer-knaflic.pdf"
reader = PdfReader(pdf)

# extract text from pdf from a particular page
page = reader.pages[5]
# print(page.extract_text())
print(pdf.getNumPages())
print(pdf.documentInfo)