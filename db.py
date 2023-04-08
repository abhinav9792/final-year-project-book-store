#for database
from sqlalchemy import create_engine,and_
import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, MetaData,DateTime,VARCHAR



engine = create_engine("sqlite:///Contact_us.db", echo=True)


# for creating table
meta = MetaData()

#table creation
Contact=Table(
    "Contact" ,meta,
    Column("s.no",Integer,primary_key=True,autoincrement=True),
    Column("name",String),
    Column("email",String),
    Column("message",String),
    Column("file_name",String,nullable=True),
    )
meta.create_all(engine)

#add unique id for each user or because right now id is used in client side session which means this id can be accessed by7 any user also id is a primary key which may cause potential harm
Register =Table(
    "Register",meta,
    Column("Id",Integer,primary_key=True,autoincrement=True),
    Column("Name",String),
    Column("Email",String),
    Column("Password",String)
)
meta.create_all(engine)

Upload_book =Table(
    "Upload_book",meta,
    Column("b_Id",Integer,primary_key=True,autoincrement=True),
    Column("name_of_book",String),
    Column("name_of_author",String),
    Column("category",String),
    Column("publisher",String),
    Column("isbn",String),
    Column("upload_book",String),
    Column("type",String),
    Column("images",String),
    Column("added_by",String)
)
meta.create_all(engine)


User_upload_book=Table(
    "User_upload_book",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("b_id",Integer),
    Column("name_of_book",String),
    Column("name_of_author",String),
    Column("file",String),
    Column("images",String),
    Column("date",String),
    Column("type",String)
)
meta.create_all(engine)

#not yet done [this function will store the information of deleted books]
archive_book=Table(
    "archive_book",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("b_id",Integer),
    Column("name_of_book",String),
    Column("file",String),
)
meta.create_all(engine)

Sell_book=Table(
    "Sell_book",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("book_id",Integer,autoincrement=True),
    Column("user_id",Integer),
    Column("name_of_book",String),
    Column("description",String),
    Column("Condition",String),
    Column("price",Integer),
    Column("time",String)
)
meta.create_all(engine)

Sell_book_images=Table(
    "Sell_book_images",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("book_id",Integer,autoincrement=True),
    Column("user_id",Integer),
    Column("time",String),
    Column("image",String)
)
meta.create_all(engine)