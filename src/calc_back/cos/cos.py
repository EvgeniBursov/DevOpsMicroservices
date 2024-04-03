import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def cosFun():
    num1 = float(flask.request.args.get('num1'))
    cos = cosine(num1)
    return flask.jsonify({'result': cos})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5002, debug = True)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def cosine(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2*n)) / factorial(2*n)
    return result
