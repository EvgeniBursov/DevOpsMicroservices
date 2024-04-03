import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def binary():
    num1 = float(flask.request.args.get('num1'))
    return flask.jsonify({'result': bin(num1)[2:]})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug = True)
