import fitz
from fitz import PDF_ENCRYPT_KEEP

pdf = fitz.open("high.pdf")

#-----------------------------------------------------#
#------------------------------------------------------
#----------HIGHLIGHT IN PDF<<<<<<<<<<------------------
#-------------------------------------------------------
print(pdf)
#to highlight pdf
ip ="While my mother rode with me in the helicopter, my father went home to check on my brother and sister and break the news to them. He choked back tears as he explained to my sister that he would miss her eighth-grade graduation ceremony that night. After passing my siblings off to family and friends, he drove to Cincinnati to meet my mother. "

for i in pdf:
    text=i.search_for(ip)
    # for highlighting text
    for j in text:
        high= i.add_highlight_annot(j)
        high.set_colors(stroke=[0.5, 0, 0]) # dark brown
        high.update()


    # for j in text:
    #     high= i.add_squiggly_annot(j)
    #     high.set_colors(stroke=[0.5, 0, 0]) # dark brown
    #     high.update()
    # for j in text:
    #     high= i.add_underline_annot(j)
    #     high.set_colors(stroke=[0.5, 0, 0]) # dark brown
    #     high.update()
        

pdf.save("high.pdf",incremental=True,encryption=PDF_ENCRYPT_KEEP)
print("saved")

