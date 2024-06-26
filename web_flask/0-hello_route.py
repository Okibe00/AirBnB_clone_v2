#!/usr/bin/python3
'''
Starts a flask application web application
'''
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    '''
    prints the string hello  world
    '''
    return ("Hello HBNB!")
if __name__ == '__main__':
    app.run()
