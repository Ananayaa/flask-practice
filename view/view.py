# this file holds all the business logic-crud operations
from database import DB

def create(fname,lname,dob,emailid,phoneno,gender):
    db=DB()
    db.cur.execute("SELECT * FROM user1")
    q=db.cur.fetchall()
    for i in q:
        print(i)
    print(fname,lname,dob,emailid,phoneno,gender)