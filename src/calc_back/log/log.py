import flask


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def log():
    try:
        num1 = flask.request.args.get('num1')
        num2 = flask.request.args.get('num2')

        if '-' in num1[0] or '-' in num2[0]:
            message = "logarithm is not defined for negative numbers."
            data = {'error': message}
            return flask.jsonify({'error': message})
        else:
            num1 = float(num1)
            num2 = float(num2)
            x = 0
            while num2**x < num1:
                x += 0.001  
            result = round(x, 5) 
            return flask.jsonify({'result': result})

    except ValueError:
        message = 'Invalid input. Please provide valid numbers.'
        return flask.jsonify({'error': message})

    except Exception as e:
        return flask.jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
