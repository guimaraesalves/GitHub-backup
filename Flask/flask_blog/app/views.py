from flask import render_template
from app import app


@app.route('/')
def index():
    animal = "Onça"
    return render_template('index.html', name=animal)
