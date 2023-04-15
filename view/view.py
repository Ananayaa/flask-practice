# this file holds all the business logic-crud operations

from database import DB

def create(fname,lname,dob,emailid,phoneno,gender):
    db=DB()
    db.cur.execute(f"INSERT INTO user1 (fname, lname, phoneno, email, dob, gender) VALUES ('{fname}','{lname}','{phoneno}','{emailid}','{dob}','{gender}')")
    db.DB.commit() 
    return "New user is created"   

def read():
    db = DB()
    db.cur.execute("select * from user1")
    res = db.cur.fetchall()
    return res

def delete():
    id=int(input("enter the number"))
    db=DB()
    db.cur.execute(f"select * from user1 where sno={id}")
    res = db.cur.fetchall()
    print(res)
    if res==[]:
         print("user does not exist")
    elif(res[0][0]==id):
        print("deleting user")
          
delete()       