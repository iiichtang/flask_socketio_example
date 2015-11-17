
from flask import render_template
import json
from flask import Flask, session
from flask import request
from flask import make_response
from flask import Response
from flask import jsonify
from flask import redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# set the secret key.  keep this really secret:


# 127.0.0.1:5000
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


# 127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    # None means do not raise the keyError if the username does not exist
    # http://stackoverflow.com/questions/20115662/what-does-the-second-argument-of-the-session-pop-method-do-in-python-flask
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)