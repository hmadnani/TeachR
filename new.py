from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/")
def home():
    return render_template('home.html', subjects= subjects, equipments= equipments, grades= grades)

@app.route("/new")
def new():
    return render_template('new.html' , title= 'new')

if __name__ == '__main__':
    app.run(debug = True)