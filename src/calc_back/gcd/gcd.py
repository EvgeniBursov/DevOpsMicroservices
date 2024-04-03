import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def gcd():
    num1 = int(flask.request.args.get('num1'))
    num2 = int(flask.request.args.get('num2'))
    while b != 0:
        a, b = b, a % b
        result = a
    return flask.jsonify({'result': result})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5004, debug = True)

