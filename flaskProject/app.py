from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('cv.html')


@app.route('/contactList')
def contact_list():
    return render_template('contactList.html')


@app.route('/assignment8')
def assignment8_fun():
    return render_template('assignment8.html', user={'name': "Amit peretz", 'gender': 'girl'}, hobbies=['dancing', 'traveling', 'yoga'])


if __name__ == '__main__':
    app.run(debug=True)