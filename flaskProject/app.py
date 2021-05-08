from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_home():
    return 'Welcome to the home page!'


@app.route('/amit')
def hello_amit():
    return 'Welcome to my page!'


@app.route('/main')
def hello_main():
    return redirect('/')


@app.route('/anotherPage')
def hello_another():
    return redirect(url_for('hello_home'))


if __name__ == '__main__':
    app.run()
