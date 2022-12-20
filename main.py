from flask import Flask,render_template,request, flash,session
from werkzeug.utils import secure_filename
from db import *
import json


#self created library
from basic_func import file_upload_pdf_test,add_image

f= open("templates//data.json","r")
s= f.read()
data=json.loads(s)

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY= data["super-secret-key"]
)


@app.route("/")
def home_page():
    #logic for stats section
    

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

    return render_template("home2.html",book=pop_books,m_books=more_books)
    
@app.route("/home1")
def home_page1():
    return render_template("Homepage.html")

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

@app.route("/login")
def login():
    return render_template("sign_in.html")

@app.route("/about")
def about_us():
    return render_template("About.html")

@app.route("/privacy")
def privacy_ploicy():
    return render_template("privacy.html")

@app.route("/tc")
def terms_and_condition():
    return render_template("tc.html")

@app.route("/book_info")
def book_info():
    return render_template("book_info.html")

#admin zone

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
        image= add_image(a,name)

        #database uploading goes here--
        u_book= Upload_book.insert().values(name_of_book=name,name_of_author=author,category=category,publisher=publisher,isbn=isbn,upload_book="static/books/"+a,type=type,images=image)
        u_book.compile().params
        conn = engine.connect()
        conn.execute(u_book)
        return "success"
    else: return "something went wrong"

    #
@app.route("/books")
def books():
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


        
if __name__ == "__main__":
    app.run(debug=True)
