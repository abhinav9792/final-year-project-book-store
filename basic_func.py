# for 1
import re

# for 3.
import fitz
import io
from PIL import Image
from datetime import datetime
import os
import shutil
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
    return name+"-page-%i.jpeg" % page.number
# $. get current date time 
def datetimes():
    now = datetime.now()
    cur_time =now.strftime("%d/%m/%Y %H:%M:%S")
    return cur_time

#5. change the size of image
def reduce_image(b):
    image = Image.open("static/book_img/"+b)
    new_image = image.resize((400,500))
    new_image.save( "static/book_img/"+b)
    return "static/book_img/"+b

print(datetimes())

#6. get images from pdf [first image]
def get_img(file,name):
    pdf_file = fitz.open("static/books/"+file)
    for page_index in range(len(pdf_file)):
    # get the page itself
        page = pdf_file[page_index]
        # get image list
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
            
            # print("[!] No images found on page", page_index)
            for image_index, img in enumerate(image_list, start=1):
                # get the XREF of the image
                
                xref = img[0]
                # extract the image bytes
                base_image = pdf_file.extract_image(xref)
                image_bytes = base_image["image"]
                # get the image extension
                image_ext = base_image["ext"]
                # load it to PIL
                image = Image.open(io.BytesIO(image_bytes))


                # save it to local disk
                image.save(open(f"static/book_img/{name}{page_index+1}_{image_index}.{image_ext}", "wb"))
                return f"{name}{page_index+1}_{image_index}.{image_ext}"
                break
            break
        break

#get the book chapter
def book_chapter(book):
    pdf = fitz.open("static/books/"+ book)
    chap=[]
    for i in range(len(pdf.get_toc())):
        chap.append(pdf.get_toc()[i])
    return chap





# name="cisco"
# get_img(file,name)


#create all the required folder
def create_folder():
    print("----------->>>>Status of folder <<<<<<<-----------")
    if os.path.exists("static"):
        print("folder static exist")
    else:
        os.mkdir("static")

    #static/book
    if os.path.exists("static/book") == True:
        print("folder static/book exist")
    else:
        os.mkdir("static/book")
    if os.path.exists("static/book_img")==True:
        print("folder static/book_img exist")
    else:
        os.mkdir("static/book_img")   
    #archive
    if os.path.exists("static/archive") == True:
        print("folder static/archive exist")
    else:
        os.mkdir("static/archive")    
    if os.path.exists("static/archive/book") == True:
        print("folder static/archive/book exist")
    else:
        os.mkdir("static/archive/book")

    if os.path.exists("static/archive/book_img")==True:
        print("folder static/archive/book_img exist")
    else:
        os.mkdir("static/archive/book_img")           
    
    if os.path.exists("static/sell_book")==True:
        print("folder static/sell_book exist")
    else:
        os.mkdir("static/sell_book")           
            
def move_file(arc_data):
    # arc_data will be the list
    shutil.move(loc+name,"archive/book")

#GET BOOK INFORMATION
def get_book_data(pdf_loc):
    book_info={}
    file = pdf_loc
    pdf = fitz.open(file)
    author =pdf.metadata["author"]
    format =pdf.metadata["format"]
    name =pdf.metadata["title"]
    time = datetimes()
    

    return author,format,name,time


print(get_book_data("static/books/CN_notes.pdf"))