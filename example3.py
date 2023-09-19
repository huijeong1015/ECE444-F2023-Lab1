from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('example3-1.html')

@app.route('/user/<name>')
def user(name):
    return render_template('example3-2.html', name=name)

