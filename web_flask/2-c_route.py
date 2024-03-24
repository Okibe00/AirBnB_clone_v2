#!/usr/bin/python3
'''
creates a web applications with following requirements

Your web application must be listening on 0.0.0.0, port 5000
Routes:
  /: display “Hello HBNB!”
  /hbnb: display “HBNB”
  /c/<text>: display “C ” followed
  by the value of the text variable(replace underscore _ symbols with a space)
You must use the option strict_slashes=False in your route definition
'''
from flask import Flask
from markupsafe import escape

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


@app.route('/c/<text>')
def args_url(text=None):
    '''
    print args passed
    '''
    text = "C {}".format(escape(text)).replace("_", " ")
    return (text)


if __name__ == '__main__':
    app.run()
