from flask import render_template
from flask import Flask

app = Flask(__name__)


# 127.0.0.1:5000/render_template
# 127.0.0.1:5000/render_template/anonymous
@app.route('/render_template/')
@app.route('/render_template/<input_name>')
def render_with_name(input_name=None):
    return render_template('get_name.html', user_name=input_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
