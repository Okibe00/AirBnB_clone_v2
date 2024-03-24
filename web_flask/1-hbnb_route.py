#!/usr/bin/python3
'''
creates a web applications with following requirements

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition
'''
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    '''
    prints Hello HBNB
    '''
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    '''
    prints hbnb
    '''
    return ('HBNB')


if __name__ == '__main__':
    app.run()
