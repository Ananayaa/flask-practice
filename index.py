from flask import Flask, render_template, request 
from view import view
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact', methods = ["POST","GET"])
def contact():
   if request.method == "POST":
      name = request.form.get("name")
      email = request.form.get("email")
      phone = request.form.get("phone")
      message = request.form.get("message")
      print(name,email,phone,message)
   return render_template('contact.html')

@app.route('/signup',methods = ["POST","GET"])
def signup():
   if request.method == "POST":
      fname = request.form.get("firstname")
      lname = request.form.get("lname")
      gender = request.form.get("gender")
      email = request.form.get("email")
      phone = request.form.get("phone")
      dob = request.form.get("dob")
      result = view.create(fname=fname,lname=lname,dob=dob,emailid=email,phoneno=phone,gender=gender)
      if result == "New user is created":
         return render_template("login.html")
      else:
         return render_template('signup.html')
   return render_template('signup.html')

@app.route('/details',methods = ["GET"])
def details():
   if request.method == "GET":
      show=view.read()
      print(show)
      return render_template('index.html',show=show)

@app.route('/login')
def login():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(host = "0.0.0.0",debug=True,port="5002")

