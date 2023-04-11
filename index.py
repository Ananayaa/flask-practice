# from flask import Flask,render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')



# # end point-http://127.0.0.1:5000/
# # context path- /ananya

# @app.route("/about")
# def ananya():
#     return render_template('about.html')

# if __name__ == '__main__':
#     app.run()
    

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('index.html')
# if __name__ == '__main__':
#    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
   
if __name__ == '__main__':
   app.run(debug=True)