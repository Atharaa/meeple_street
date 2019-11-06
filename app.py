from flask import Flask 
app = Flask(__name__)

name = "Ben"
nb1 = 12
nb2 = 2
@app.route('/')
def index():
    return 'Jurassic Park Index'
@app.route('/say_hello/<name>')
def hello_world(name):
    return 'Hello World %s' % name
@app.route('/multiply/<int:nb1>/<int:nb2>')
def multiply(nb1, nb2):
    return "%s" % (nb1 * nb2)