import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def sinFun():
    num1 = float(flask.request.args.get('num1'))
    sin_param = sin(num1)
    return flask.jsonify({'result': sin_param})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5007, debug = True)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sin(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result







