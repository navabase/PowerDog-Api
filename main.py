#!flask/bin/python
from flask import Flask
from flask import render_template
import api

dog = api.PowerDog("test@mail.com","sfoq3fp3q2jf")

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api')
def Api():
    return "incomming"

if __name__ == '__main__':
    app.run(debug=True)