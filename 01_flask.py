from flask import render_template
import json
from flask import Flask, session
from flask import request
from flask import make_response
from flask import Response
from flask import jsonify
from flask import redirect
from flask import url_for

app = Flask(__name__)


# 127.0.0.1:5000
@app.route('/')
def hello_world_string():
    return "hello world"


# 127.0.0.1:5000/return_json
@app.route('/return_json')
def hello_world_json():
    data = {"first key": "hello", "second key": "world", "word count": 2}
    result = json.dumps(data, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None,
                        indent=True, separators=None, encoding="utf-8", default=None, sort_keys=False)

    # method 1
    resp = make_response(result)

    if request.headers.get('Accept', '').find('application/json') > -1:
        resp.mimetype = 'application/json'
    else:
        resp.mimetype = 'text/plain'

    """
    # method 2 (can define mimitype)
    resp = Response(result, status=200, mimetype='application/json')

    # method 3 (no need to use json.dump)
    resp = jsonify(data)

    if request.headers.get('Accept', '').find('application/json') > -1:
        resp.mimetype = 'application/json'
    else:
        resp.mimetype = 'text/plain'
    """

    return resp



# 127.0.0.1:5000/return_html
@app.route('/return_html')
def hello_world_html():
    return render_template('test.html')


# 127.0.0.1:5000/return_html_2
@app.route('/return_html_2')
def hello_world_html_2():
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


# 127.0.0.1:5000/redirect
@app.route('/redirect')
def redirect_to_other_api():
    return redirect(url_for('hello_world_string'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
    # threaded=True -> multi-thread
    # processes=3 -> open
    # http://werkzeug.pocoo.org/docs/0.11/serving/#werkzeug.serving.run_simple