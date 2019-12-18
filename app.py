from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/hello/<name>')
def hello(name):
	return 'Hello, {}'.format(name)

if __name__ == '__main__':
    app.run()
