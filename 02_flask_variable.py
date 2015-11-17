from flask import Flask
from flask import request

app = Flask(__name__)


# 127.0.0.1:5000/variable/abcde
@app.route('/variable/<input_value>')
def show_input_value(input_value):
    return 'the input value is: %s' % input_value


# 127.0.0.1:5000/int_variable/100
# 127.0.0.1:5000/int_variable/abcde
@app.route('/int_variable/<int:input_value>')
def show_int_value(input_value):
    return 'the input value ^2 is: %d' % (input_value ** 2)


# 127.0.0.1:5000/path_variable/abcde/dfsd/dsf
@app.route('/path_variable/<path:input_value>')
def show_path_value(input_value):
    return 'the path: %s' % input_value


"""
accept variable: int, float, path(can get /)
"""


# 127.0.0.1:5000/multiple_variable/test1&test2
@app.route('/multiple_variable/<input_value_1>&<input_value_2>')
def show_multiple_value(input_value_1, input_value_2):
    return 'value 1 = %s and value 2 = %s' % (input_value_1, input_value_2)


# 127.0.0.1:5000/request_variable?name=Joe+Soap&age=21
@app.route('/request_variable')
def show_request_value():
    name = request.args.get('name')
    age = request.args.get('age')
    return 'name = %s and age = %s' % (name, age)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
