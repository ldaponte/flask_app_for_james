from flask import Flask, request

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    """Route that takes a name parameter in the URL path"""
    return f"hello {name}"

@app.route('/hello')
def hello_query():
    """Route that takes a name parameter as a query string"""
    name = request.args.get('name', 'world')
    return f"hello {name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
