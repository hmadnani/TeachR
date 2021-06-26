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

class Form(FlaskForm):
    Subject = SelectField('Subject', choices = [('maths'), ('english'), ('science'), ('art')])
    Grade = SelectField('Grade', choices=[1,2])

@app.route('/', methods= ['GET', 'POST'])
def index():
    form = Form()
    # form.Grade.choices = [(Grade) for Grade in Resources]

    return render_template('new.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
