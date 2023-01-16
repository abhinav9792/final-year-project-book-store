from flask import Flask,render_template,request, flash,session
from werkzeug.utils import secure_filename
from db import *
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete


#self created library
from basic_func import file_upload_pdf_test,add_image,reduce_image,datetimes,get_img

f= open("templates//data.json","r")
s= f.read()
data=json.loads(s)


app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY= data["super-secret-key"]
)

#connect to engine


@app.route("/")
def home_page():
    #logic for stats section
    Session = sessionmaker(bind = engine)
    session = Session()
 
    # SELECT COUNT(*) FROM Actor
    stats=[]
    no_of_books = session.query(Upload_book).count()
    stats.append(no_of_books)
    
    #logic for displaying books on popular books section
    conn = engine.connect()
    shows = Upload_book.select().where(Upload_book.c.images != " ")
    result =conn.execute(shows)
    pop_books= result.fetchall()


    #logic for more books
    conn = engine.connect()
    shows = Upload_book.select().where(Upload_book.c.images != " ")
    result =conn.execute(shows)
    more_books= result.fetchall()

    return render_template("home2.html",book=pop_books,m_books=more_books,stats=stats)
#--------------->>>>>>>CONTACT US<<<<<<<<<<-------------------------#
@app.route("/contact")
def contact_us():
    return render_template("Contact_us.html")

@app.route("/contact1",methods=["GET","POST"])
def contact_us1():
    if request.method == "POST":
        name = request.form["name"]
        ea = request.form["email"]
        # r = request.form["reason"]
        msg = request.form["message"]
        f = request.files['file']
        a= secure_filename(f.filename)
        f.save("static/"+a)

        ins =Contact.insert().values(name =name,email=ea,message=msg,file_name="static/"+a)
        ins.compile().params

        # # for adding the data into the database
        conn = engine.connect()
        result = conn.execute(ins)
        flash("you have submmited your form")
        #return  render_template("contact_us_data.html")
        return f"submiited here are the details,{name}, and other details are"
    else:
        return "<h1> no found </h1>"
#---------------->>>>>>>>>>REGISTER<<<<<<<<------------------------#
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_done",methods=["GET","POST"])
def register_done():
    if request.method=="POST":
        name = request.form["name"]
        ea = request.form["email"]
        password =request.form["password"]
        #tc= request.form["tc"]
        print(name,ea,password)
        register= Register.insert().values(Name=name,Email=ea,Password=password)
        register.compile().params
        conn = engine.connect()
        conn.execute(register)
        flash("you have been registered")
        return render_template("register.html")
#---------->>>>>>>LOGIN/SIGNUP<<<<<<<-----------------#
@app.route("/login")
def login():
    return render_template("sign_in.html")

@app.route("/login_next",methods=["GET","POST"])
def login_next():
    if request.method =="POST":
        u_name=request.form["u_name"]
        p_word =request.form["p_word"]
# this logic  is wroking but when we enter the wrong password it throws "list out of bound error"wrong credentails
# possible idea to fix
# 1. use try except
# 2. throw error
# 3. using empty list logic 
        Session = sessionmaker(bind = engine)
        reg_session = Session()
        login = reg_session.query(Register).filter((Register.c.Email.like(u_name)) & Register.c.Password .like(p_word)) 

        if login != []:
            for i in login:
                print(i)
            data=i
            print(data[1])
            session["value"] = data[0]
            log=data

            #getting users book 
            conn = engine.connect()
            u_shows = User_upload_book.select().where(User_upload_book.c.b_id == log[0])
            result =conn.execute(u_shows)
            u_books= result.fetchall()
            print("------>>>>>",u_books)


            # logic for stats section
            u_stats=[]
            no_of_books = reg_session.query(User_upload_book).count()
            u_stats.append(no_of_books)
           
            return render_template("profile page for user.html",log=log,book_list=u_books,u_stats=u_stats)
        else: return "wrong login information"
    else:return render_template("sign_in.html")


@app.route("/book_user",methods=["GET","POST"])
def book_user():
    if "value" in session:
        sess= session['value'] 
        print("----->>>session value",sess)
        if request.method =="POST":
            book_name=request.form["book_name"]
            author=request.form["author"]
           
            file= request.files["book"]
            a= secure_filename(file.filename)
            #this function is testing for file is pdf or not ??
            a= file_upload_pdf_test(a)
            file.save("static/books/"+a)
            type = request.form["type"]

                #implement here
            b=get_img(a,book_name)
            image=reduce_image(b)
            time=datetimes()
            
            print(f"BOOK NAME ------>>>>name",{book_name},"author",{author},"type",{type},"image",{image},"pdf type",{a},"date",{time})

                #database uploading goes here--
            u_book= User_upload_book.insert().values(b_id=sess,name_of_book=book_name,name_of_author=author,file="static/books/"+a,type=type,images=image,date=time)

            u_book.compile().params
            conn = engine.connect()
            conn.execute(u_book)
            
            return "<h1> success </h1>"
        else: return "<h1> abc not uploaded</h1>"
    else : return "<h1> please login </h1>"

@app.route("/about")
def about_us():
    return render_template("About.html")

@app.route("/privacy")
def privacy_ploicy():
    return render_template("privacy.html")

@app.route("/tc")
def terms_and_condition():
    return render_template("tc.html")

@app.route("/book_info/<path:book_name>")
def book_info(book_name):
    conn = engine.connect()
    shows = Upload_book.select().where(Upload_book.c.name_of_book == book_name)
    result =conn.execute(shows)
    res= result.fetchone()
    for i in res:
        print("---->>>your res--",i)
    return render_template("book_info.html",res=res)



@app.route("/book_category")
def book_cateogry():
    return render_template("book_category.html")

#---------->>>>>>OPEN PDF SECTION<<<<----------------------#
@app.route("/pdf")
def open_pdf():
    return render_template("open_pdf.html")
    
#--------------------------------------------------------------------------------------#
#---------------------->>>>>>>>ADMIN ZONE<<<<<<<<<<<<<<<------------------------------#
#--------------------------------------------------------------------------------------#

@app.route("/admin_login")
def login_admin():
    return render_template("sign2.html")

@app.route("/admin_login_next", methods=["GET","POST"])
def admin_login_next():
    if request.method =="POST":
        u_name=request.form["u_name"]
        p_word =request.form["p_word"]
        
        if u_name == data[u_name]["u_name"] and p_word== data[u_name]["p_word"] :
            session["value"] = data[u_name]
            sess =session.get("value")
            sess = data[u_name]
            
            return render_template("admin_Zone.html",sess=sess)
        else:
            return '<h1 style="background-color:red; font-size:40px; color:white; text-align:center;"> something went wrong </h1>'
    else:
        return "<h1> Wrong method for accessing this page ie [GET,POST] </h2>"

@app.route("/admin_test")
def admin_zone():
    return render_template("admin_zone.html")

@app.route("/logout")
def logout():
    session.pop("value",None)
    return render_template("sign2.html")

@app.route("/contact_data")
def contact_data():
    #if('value' in session and session['value'] == user['username']):
    if "value" in session:
        sess= session['value'] 
        conn = engine.connect()
        shows = Contact.select()
        result =conn.execute(shows)
        rows= result.fetchall()
        return render_template("contact_us_data.html",data = rows,sess=sess)
    else: return "please login"

@app.route("/register_data")
def register_data():
    if "value" in session:
        sess= session['value'] 
        conn = engine.connect()
        shows= Register.select()
        result = conn.execute(shows)
        rows = result.fetchall()
        return render_template("register_data.html",data= rows,sess=sess)
    else: return "please login"
#----------------->>>>>>>>>> book section<<<<<<<<-----------------#
@app.route("/manage_book")
def manage_book():
    if "value" in session:
        sess= session['value'] 
        return render_template("manage_books.html",sess=sess)

@app.route("/upload_book")
def upload_book():
    if "value" in session:
        sess= session['value'] 
        return render_template("upload_books.html",sess=sess)
    else: return "please login"

@app.route("/upload_page", methods=["GET","POST"])
def upload_page():
    if "value" in session:
        sess= session['value']
        if request.method =="POST":
            name= request.form["name_of_book"]
            author= request.form["name_of_author"]
            category= request.form["category"]
            publisher= request.form["publisher"]
            isbn= request.form["isbn"]
            file= request.files["upload_book"]
            a= secure_filename(file.filename)
            #this function is testing for file is pdf or not ??
            a= file_upload_pdf_test(a)
            file.save("static/books/"+a)
            type = request.form["type"]
            
            #implement here
            b=get_img(a,name)
            image=reduce_image(b)


            #database uploading goes here--
            u_book= Upload_book.insert().values(name_of_book=name,name_of_author=author,category=category,publisher=publisher,isbn=isbn,upload_book="static/books/"+a,type=type,images=image,added_by=sess["name"])

            u_book.compile().params
            conn = engine.connect()
            conn.execute(u_book)
            return "success "
        else: return "something went wrong"
    else: return "Please login"

    #
@app.route("/books",methods=["GET","POST"])
def books():
    if request.method == "POST":
        id=request.form["id"]
        a=Upload_book.delete().where(Upload_book.c.b_Id == id)
        conn = engine.connect()
        conn.execute(a)
    if "value" in session:
        sess= session['value'] 
        conn =engine.connect()
        books =Upload_book.select()
        result= conn.execute(books)
        rows= result.fetchall()
        return render_template("books.html",books=rows,sess=sess)
    
    else: return "<h1> please login </h1>"

@app.route("/general_setting")
def general_settings():
    if "value" in session:
        sess=session["value"]
        return render_template("general_settings.html",sess=sess)
    else: return "please login"

@app.route("/performance")
def performance():
    if "value" in session:
        sess=session["value"]
        return render_template("chart.html",sess=sess)
    else:return "please login"

# ------------------>need some work <<<<<<<<<<<---------
@app.route("/book_test")
def book_test():
    if "value" in session:
        sess=session["value"]
        conn =engine.connect()
        books =Upload_book.select()
        result= conn.execute(books)
        rows= result.fetchall()
        return render_template("books_test.html",books=rows,sess=sess)


        
if __name__ == "__main__":
    app.run(debug=True)
