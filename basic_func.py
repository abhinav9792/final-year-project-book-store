import re
from PIL import Image

# 1 .
#code for checking if the uploaded file is pdf or not
def file_upload_pdf_test(string):
    x=re.findall(".pdf+$",string)
    if (x):
        return string
    else:
        print(0)

# file_upload_pdf_test(string)
#2.
def reduce_image_size():
    foo = Image.open('static/1.jpg')  # My image is a 200x374 jpeg that is 102kb large
    foo.size  # (200, 374)
    
    #downsize the image with an ANTIALIAS filter (gives the highest quality)
    height= int(input())
    width = int(input())
    foo = foo.resize((height,width),Image.ANTIALIAS)
    foo.save('path/to/save/image_scaled_opt.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb
