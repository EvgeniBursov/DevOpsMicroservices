import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def gcd():
    num1 = flask.request.args.get('num1')
    num2 = flask.request.args.get('num2')

    if '.' in num1 or '.' in num2:
        message = "GCD is not defined for float numbers."
        data = {'error': message}
        return flask.jsonify({'result': data})   
    else:
        num1 = int(num1)
        num2 = int(num2)
    if num1 == 0:
        return flask.jsonify({'result': num2})
    if num2 == 0:
        return flask.jsonify({'result': num1})

    while num2 != 0:
        num1, num2 = num2, num1 % num2
        result = num1
    return flask.jsonify({'result': result})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5004, debug = True)

