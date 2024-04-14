import flask


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def fib():
    try:
        num1 = flask.request.args.get('num1')
        num2 = flask.request.args.get('num2')

        if '-' in num1[0] or '-' in num2[0] or '.' in num1[0] or '.' in num2[0]:
            message = 'fibonachi can be float or negative'
            return flask.jsonify({'error': message})
        else:
            num1 = int(num1)
            num2 = int(num2)
            fib_sequence = [0, 1]
            while len(fib_sequence) < num1:
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            result = fib_sequence
            return flask.jsonify({'result': result})

    except ValueError:
        message = 'Invalid input. Please provide valid numbers.'
        return flask.jsonify({'error': message})

    except Exception as e:
        return flask.jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
