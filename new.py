from flask import Flask, render_template

app = Flask(__name__)

subjects = [
    {'sub': 'Maths'},
    {'sub': 'English'},
    {'sub': 'Science'},
    {'sub': 'Art'},
]

equipments = [
    {'Equip': 'Projector'},
    {'Equip': 'Laptop'},
    {'Equip': 'Tablet'},
    {'Equip': 'Smartboard'},
    {'Equip': 'Camera'},
    {'Equip': 'Printer'},
    {'Equip': '3D Printer'},
    {'Equip': 'No Equiment Available'},

]

grades = [
    {'grade': '1'},
    {'grade': '2'}
]

Types = [
    {'type': 'Remote'},
    {'type': 'Classroom'}
]
@app.route("/")
def home():
    return render_template('home.html', subjects= subjects, equipments= equipments, grades= grades, Types=Types)

@app.route("/math")
def new():
    return render_template('math.html' , title= 'math')

if __name__ == '__main__':
    app.run(debug = True)