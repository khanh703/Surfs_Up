from flask import Flask

# This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code is being 
# run from the command line or if it has been imported into another 
# piece of code. Variables with underscores before and after them are 
# called magic methods in Python.
app = Flask(__name__)


# starting point, also known as the root
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/login')
def login():
    return 'You have reached login'