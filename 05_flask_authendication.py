from flask import Flask
from flask import request
from flask import Response

from functools import wraps

app = Flask(__name__)


def check_auth(username, password):
    """
    This function is called to check if a username / password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            # no authenticate information
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            # username or password not correct
            return authenticate()
        return f(*args, **kwargs)

    return decorated


# curl -v -u "admin:secret" http://127.0.0.1:5000/authendicate_test
@app.route('/authendicate_test')
@requires_auth
def login_check():
    return "You have successfully pass the login check"
    # return render_template('target.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
