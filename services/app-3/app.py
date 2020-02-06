from flask import Flask, escape, request


app = Flask(__name__)


@app.route('/')
def hello():
    return f'This is app 3!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')