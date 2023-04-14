from flask import Flask, render_template, request 
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

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/login')
def login():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(host = "0.0.0.0",debug=True,port="5001")

