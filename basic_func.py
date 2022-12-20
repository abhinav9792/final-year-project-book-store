# for 1
import re

# for 3.
import fitz
import io
from PIL import Image
from datetime import datetime
# 1 .
#code for checking if the uploaded file is pdf or not
def file_upload_pdf_test(string):
    x=re.findall(".pdf+$",string)
    if (x):
        return string
    else:
        print(0)

# file_upload_pdf_test(string)
#2,
def reduce_image_size():
    foo = Image.open('static/1.jpg')  # My image is a 200x374 jpeg that is 102kb large
    foo.size  # (200, 374)
    
    #downsize the image with an ANTIALIAS filter (gives the highest quality)
    height= int(input())
    width = int(input())
    foo = foo.resize((height,width),Image.ANTIALIAS)
    foo.save('path/to/save/image_scaled_opt.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb

#3.
#fucntion to get images from the pdf

def add_image(book,name):
    file = "static/books/"+book

    pdf = fitz.open(file)
    
    # print(pdf.page_count)
    # print(pdf.metadata)
    #get index
    #print("toc",pdf.get_toc())
    #print(pdf.load_page(1)
    page = pdf.load_page(1)  # loads page number 'pno' of the document (0-based)
    pix = page.get_pixmap()
    pix.save("static/book_img/"+name+"-page-%i.jpeg" % page.number)
    print("image added successfully")
    return "static/book_img/"+name+"-page-%i.jpeg" % page.number

def datetimes():
    now = datetime.now()
    cur_time = now.strftime("%d/%m/%Y %H:%M:%S")
    return cur_time

print(datetimes())