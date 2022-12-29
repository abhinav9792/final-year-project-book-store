#for database
from sqlalchemy import create_engine,and_
import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, MetaData,DateTime



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
    Column("added_by",String),
    Column("date",DateTime),

)
meta.create_all(engine)