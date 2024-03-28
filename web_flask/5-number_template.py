#!/usr/bin/python3
'''
creates a web applications with following requirements

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”

    /hbnb: display “HBNB”

    /c/<text>: display “C ” followed by the value of the text variable
   (replace underscore _ symbols with a space)

    /python/<text>: display “Python ”, followed by the value of the
    text variable(replace underscore _ symbols with a space )
    The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition
'''
from flask import Flask
from flask import url_for
from markupsafe import escape
from flask import render_template


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
def C_url(text=None):
    '''
    print args passed
    '''
    text = "C {}".format(escape(text)).replace("_", " ")
    return (text)


@app.route('/python/<text>')
@app.route('/python')
def python_url(text="is cool"):
    '''
    print args passed
    '''
    text = "Python {}".format(escape(text)).replace("_", " ")
    return (text)


@app.route('/number/<int:n>')
def display_num(n):
    '''
    display the number passed in route
    '''
    return (f'{n} is a number')


@app.route('/number_template/<int:n>')
def display_html(n):
    '''
    display html page only if n is an int
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
