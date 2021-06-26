from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

class Resources (db.Model):
    Subject = db.Column(db.String(100))
    Grade = db.Column(db.Integer)
    Equipment_required = db.Column(db.String(500))
    URL = db.Column(db.String(500), unique = True, primary_key=True)

subjects = [
    {'sub': 'maths'},
    {'sub': 'english'},
    {'sub': 'science'},
    {'sub': 'art'},
]

equipments = [
    {'Equip': 'Projector'},
    {'Equip': 'Laptop'},
    {'Equip': 'Tablet'},
    {'Equip': 'Smartboard'},
    {'Equip': 'Camera'},
    {'Equip': 'Printer'},
    {'Equip': '3D Printer'},
    {'Equip': 'Games'},
    {'Equip': 'No Equiment Available'},

]

grades = [
    {'grade': '1'},
    {'grade': '2'}
]

class Form(FlaskForm):
    Subject = SelectField('Subject', choices = subjects)
    Grade = SelectField('Grade', choices=grades)
    Equipment = SelectField('Equipments', choices=equipments)

@app.route('/', methods= ['GET', 'POST'])
def home():
    form = Form()
    return render_template('home.html', subjects= subjects, equipments= equipments, grades= grades, form=form)

@app.route("/new")
def new():
    return render_template('new.html' , title= 'new')

if __name__ == '__main__':
    app.run(debug = True)