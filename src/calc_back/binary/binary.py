import flask
import struct 

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def binary():
    try:
        num1 = flask.request.args.get('num1')
        num2 = flask.request.args.get('num2')


        if '-' in num1[0] or '-' in num2[0]:
            message = "This binary only for positive numbers"
            data = {'error': message}
            return flask.jsonify({'error': message})

        if '.' not in num1:
            num1 = int(num1)
            newNum = 'binary operation: \n' + str(bin(num1)[2:])
            return flask.jsonify({'result': newNum})
        else:
            num1 = float(num1)
            packed = struct.pack('!f', num1)
            binary = ''.join(f'{byte:08b}' for byte in packed)
            result = 'binary operation: \n' + str(binary)
            return flask.jsonify({'result': result})

    except Exception as e:
        return flask.jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug = True)
