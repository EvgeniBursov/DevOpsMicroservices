import flask
import requests

app = flask.Flask(__name__)

port_map = {
    'factorial': 5000,
    'binary': 5001,
    'log': 5002,
    'root': 5003,
    'gcd': 5004,
    'exp': 5005,
    'fib': 5006,
}

@app.route('/', methods = ['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('calc.html')
    
    num1 = flask.request.form.get('num1')
    num2 = flask.request.form.get('num2')
    if num1 == '' and num2 == '':
        message = 'Please fill the fields'
        return flask.render_template('calc.html', result={'error': message})
    elif num1 == '':
        num1 = num2
    elif num2 == '':
        num2 = num1

    operation = flask.request.form.get('operation')


    if operation not in port_map.keys():
        message = 'Invalid Operation'
        return flask.render_template('calc.html', result={'error': message})

    url = f'http://{operation}:{port_map[operation]}/'
    
    if any((char.isalpha() for char in num1) or (char.isalpha() for char in num2)):
        message = "please use only numbers"
        return flask.render_template('calc.html', result={'error': message})
    if any((char in num1 for char in "!@#$%^&*()\/") or (char in num2 for char in "!@#$%^&*()\/")):
        message = "please dont use !@#$%^&*()\/"
        return flask.render_template('calc.html', result={'error': message})
   
    #result = requests.get(url, params = {
    #    'num1': num1,
    #    'num2': num2
    #}).json()['result']


    try:
        response = requests.get(url, params={'num1': num1, 'num2': num2})
        result = response.json()['result']
        return flask.render_template('calc.html', result={'result': result})
    except requests.exceptions.ConnectionError as e:
        error_message = f"Failed to connect to the {operation} service."
        return flask.render_template('calc.html', result={'error': error_message})
    

    

    return flask.render_template('calc.html', result = {
        #'num1': num1,
        #'num2': num2,
        #'operation': operation,
        #'result': result if isinstance(result, bool) else round(result, 3)
        'result': result
    })



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4444, debug = True)




