import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])

def factorial():
    try:
        num1 = flask.request.args.get('num1')
        num2 = flask.request.args.get('num2')
        if '-' in num1[0] or '-' in num2[0]:
            message = "Factorial is not defined for negative numbers."
            data = {'error': message}
            return flask.jsonify({'error': message})
            
        if '.' in num1 or '.' in num2:
            message = "Factorial is not defined for float numbers."
            data = {'error': message}
            return flask.jsonify({'error': message})
        
        num1 = int(num1)
        num2 = int(num2)

        if num1 == 0:
            return 1
        else:
            resultForNum1 = 1
            resultForNum2 = 1
            for i in range(1, num1 + 1):
                resultForNum1 *= i
            for i in range(1, num2+1):
                resultForNum2 *= i 
            return flask.jsonify({'result': resultForNum1})
        
    except Exception as e:
        return flask.jsonify({'result': str(e)})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)




