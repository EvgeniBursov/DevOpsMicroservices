import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def root():
    num1 = flask.request.args.get('num1')
    num2 = flask.request.args.get('num2')

    if '-' in num1 or '-' in num2:
        message = "Root cant be negative"
        data = {'error': message}
        return flask.jsonify({'error': message})
    
    if '.' in num2:
        message = "Root is not can be float numbers."
        data = {'error': message}
        return flask.jsonify({'error': message})
    else:
        num1 = float(num1)
        num2 = int(num2)
        if num2 == 0:
            message = "Root is not can be 0"
            data = {'error': message}
            return flask.jsonify({'error': message})
        if num1 == 0:
            res = 0
            return flask.jsonify({'result': res})
    
    guess = num1 / 2
    for _ in range(100):
        guess = ((num2 - 1) * guess + num1 / guess ** (num2 - 1)) / num2
    resultStr = str(guess)
    return flask.jsonify({'result': 'root operation: \n' + resultStr}) 



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5003, debug = True)




