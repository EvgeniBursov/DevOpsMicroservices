import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def power():
    try:
        num1 = flask.request.args.get('num1')
        num2 = flask.request.args.get('num2')

        if '.' in num2:
            message = "pow is not defined for float numbers."
            data = {'error': message}
            return flask.jsonify({'error': message})
        
        if '.' in num1:
            num1 = float(num1)
        else:
            num1 = int(num1)

        if '-' in str(num1)[0]:
            num1 = -abs(num1)

        num2 = int(num2)

        result = None

        if '-' in str(num2)[0]:
            result = 1 / (num1 ** abs(num2))
        else:
            result = num1 ** num2
        
        resultStr = str(result)
        return flask.jsonify({'result': 'power operation: \n' + resultStr})

                
    except Exception as e:
        return flask.jsonify({'result': str(e)})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5005, debug = True)



