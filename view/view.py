# this file holds all the business logic-crud operations

from database import DB

def create(fname,lname,dob,emailid,phoneno,gender):
    db=DB()
    db.cur.execute(f"INSERT INTO user1 (fname, lname, phone, email, dob, gender) VALUES ('{fname}','{lname}','{phoneno}','{emailid}','{dob}','{gender}')")
    db.DB.commit() 
    return "New user is created"   

def read():
    db = DB()
    db.cur.execute("select * from user1")
    res = db.cur.fetchall()
    return res
