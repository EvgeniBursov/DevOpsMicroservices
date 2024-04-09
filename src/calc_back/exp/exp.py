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
            return flask.jsonify({'result': data})
        
        if '.' in num1:
            num1 = float(num1)
        else:
            num1 = int(num1)

        if '-' in str(num1)[0]:
            num1 = abs(num1)

        num2 = int(num2)

        result = None

        if '-' in str(num2)[0]:
            result = 1 / (num1 ** abs(num2))
        else:
            result = num1 ** num2

        return flask.jsonify({'result': result})

                
    except Exception as e:
        return flask.jsonify({'result': str(e)})
"""



        
        if '-' in num1[0]:
            if '.' in num1:
                res = 1
                num1 = -abs(float(num1))
                if '-' in num2[0]:
                    num2 = int(num2)
                    for _ in range(num2):
                        res /= num1
                    return flask.jsonify({'result': res})
                else:
                    res = 1
                    num1 = -abs(int(num1))
                    num2 = int(num2)
                    for _ in range(num2):
                        res *= num1
                    return flask.jsonify({'result': res})
            else:
                if '.' in num1:
                    num1 = float(num1)
                else:
                    num1 = int(num1)
                if '-' in num2[0]:
                    num2 = abs(int(num2))
                    newNum = 1 // (num1 ** num2)
                    return flask.jsonify({'result': newNum})
                else:
                    return flask.jsonify({'result': num1*num2})
"""


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5005, debug = True)



