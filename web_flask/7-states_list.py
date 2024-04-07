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
from flask import render_template
from models import storage
from models.state import State
from flask import g


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def end_session(exception=None):
    '''close database session'''
    storage.close()


@app.route('/states_list')
def list_states():
    '''
    display a html page inside the body tag
    '''
    state_obj = list()
    state_lists = storage.all(State)
    for state_dic in state_lists:
        state_obj = state_obj + list(state_dic.values())

    state_obj = sorted(state_obj, key=lambda x: x.name)
    return render_template('7-states_list.html', state_lists=state_obj)


if __name__ == '__main__':
    app.run(debug=True)
