import fitz
doc = fitz.open("MACHINE LEARNING FOR DUMMIES.pdf") # new or existing PDF
page = doc.new_page() # new page, or choose doc[n]
r1 = fitz.Rect(50,100,100,150) # a 50x50 rectangle
disp = fitz.Rect(55, 0, 55, 0) # add this to get more rects
r2 = r1 + disp # 2nd rect
r3 = r1 + disp * 2 # 3rd rect
r4 = r1 + disp * 3 # 4th rect
t1 = "text with rotate = 0." # the texts we will put in
t2 = "text with rotate = 90."
t3 = "text with rotate = -90."
t4 = "text with rotate = 180."
red = (1,0,0) # some colors
gold = (1,1,0)
blue = (0,0,1)
"""We use a Shape object (something like a canvas) to output the text and
the rectangles surrounding it for demonstration.
"""
shape = page.new_shape() # create Shape
shape.draw_rect(r1) # draw rectangles
shape.draw_rect(r2) # giving them
shape.draw_rect(r3) # a yellow background
shape.draw_rect(r4) # and a red border

# Now insert text in the rectangles. Font "Helvetica" will be used
# by default. A return code rc < 0 indicates insufficient space (not checked here).
rc = shape.insert_textbox(r1, t1, color = blue)
rc = shape.insert_textbox(r2, t2, color = blue, rotate = 90)
rc = shape.insert_textbox(r3, t3, color = blue, rotate = -90)
rc = shape.insert_textbox(r4, t4, color = blue, rotate = 180)
shape.commit() # write all stuff to page /Contents
doc.save("test.pdf")
