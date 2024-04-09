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
            return flask.jsonify({'result': data})

        if '.' not in num1:
            num1 = int(num1)
            newNum = str(bin(num1)[2:])
            return flask.jsonify({'result': newNum})
        else:
            num1 = float(num1)
            packed = struct.pack('!f', num1)
            binary = ''.join(f'{byte:08b}' for byte in packed)
            result = str(binary)
            return flask.jsonify({'result': result})

            
        """
        
        if '.' in num1 or '.' in num2:
            integer_part1 = int(num1)
            fractional_part1 = float(num1) - integer_part1
            binary_integer_part1 = bin(integer_part1)[2:]
            binary_fractional_part1 = ''
            while fractional_part1 != 0:
                fractional_part1 *= 2
                if fractional_part1 >= 1:
                    binary_fractional_part1 += '1'
                    fractional_part1 -= 1
                else:
                    binary_fractional_part1 += '0'
        else:
            binary_integer_part1 = int(num1)
            binary_integer_part1 = bin(binary_integer_part1)[2:]
        
        if '.' in num2:
            integer_part2 = int(num2)
            fractional_part2 = num1 - integer_part2
            binary_integer_part2 = bin(integer_part2)[2:]
            binary_fractional_part2 = ''
            while fractional_part2 != 0:
                fractional_part2 *= 2
                if fractional_part2 >= 1:
                    binary_fractional_part2 += '1'
                    fractional_part2 -= 1
                else:
                    binary_fractional_part2 += '0'


        if binary_fractional_part1 != '':
            resultForNum1 = binary_integer_part1 + '.' + binary_fractional_part1
            return flask.jsonify({ 'result': resultForNum1 })
        else:
            resultForNum1 = binary_integer_part1
            flask.jsonify({ 'result': resultForNum1 })
        
        """

        """
        
        elif binary_integer_part1 and binary_integer_part2:
            resultForNum1 = binary_integer_part1
            resultForNum2 = binary_integer_part2
            return flask.jsonify({'result': resultForNum1,'result':resultForNum2})
        
        elif binary_fractional_part1 and binary_integer_part2:
            resultForNum1 = binary_integer_part1 + '.' + binary_fractional_part1
            resultForNum2 = binary_integer_part2
            return flask.jsonify({'result': resultForNum1, 'result': resultForNum2})
        
        elif binary_fractional_part2 and binary_integer_part1:
            resultForNum1 = binary_integer_part1
            resultForNum2 = binary_integer_part2 + '.' + binary_fractional_part2
            return flask.jsonify({'result': resultForNum1, 'result': resultForNum2})
        """ 
        
    except Exception as e:
        return flask.jsonify({'result': str(e)})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug = True)
