import json
from flask import Flask
from flask import request

app = Flask(__name__)


# 127.0.0.1:5000/http_get
@app.route('/http_get', methods=['GET'])
def http_get():
    return "this is the  get method"


# curl -H "Content-type: text/plain" -X POST http://127.0.0.1:5000/http_post -d 'this is a message'
# curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/http_post -d '{"message":"Hello Data"}'
# curl -H "Content-type: application/octet-stream" -X POST http://127.0.0.1:5000/http_post --data-binary @xxxxx.xxxxx
@app.route('/http_post', methods=['POST'])
def post_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./test.sh', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "Unsupported Media Type(415)"


# curl -X GET http://127.0.0.1:5000/http_both
# curl -X POST http://127.0.0.1:5000/http_both
@app.route('/http_both', methods=['GET', 'POST', 'PUT'])
def http_both():
    if request.method == 'GET':
        return 'You are using the GET method'
    elif request.method == 'POST':
        return 'You are using the POST method'
    else:
        return 'The method is: %s ' % request.method


"""
available http methods:
GET
HEAD
POST
PUT
DELETE
OPTIONS
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
