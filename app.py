from flask import Flask, jsonify,render_template,request,redirect
from flask_fontawesome import FontAwesome
from flask_restful import Resource ,Api, reqparse, abort , fields , marshal_with
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
fa = FontAwesome(app)



@app.route('/')
def Home():

    return render_template('index.html')
    # return 

@app.route('/about')
def about():

    return render_template('about.html')
    # return 

@app.route('/service')
def service():

    return render_template('service.html')
    # return 

@app.route('/portfolio')
def portfolio():

    return render_template('portfolio.html')
    # return 

@app.route('/contact')
def contact():

    return render_template('contact.html')
    # return 
















if __name__ == '__main__':
      
    app.run(debug = True)