from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home_page():
    return render_template('cv.html')


@app.route('/contactList')
def contact_list():
    return render_template('contactList.html')


@app.route('/assignment8')
def assignment8_fun():
    return render_template('assignment8.html', user={'name': "Amit peretz", 'gender': 'girl'}, hobbies=['dancing', 'traveling', 'yoga'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_fun():
    search, username, = '', ''
    users1 = ({"id": 1, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris",
                  "avatar": "https://reqres.in/img/faces/5-image.jpg"},
              {"id": 2, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth",
                  "avatar": "https://reqres.in/img/faces/1-image.jpg"},
              {"id": 3, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
                  "avatar": "https://reqres.in/img/faces/2-image.jpg"},
              {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt",
                  "avatar": "https://reqres.in/img/faces/4-image.jpg"},
              {"id": 5, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong",
                  "avatar": "https://reqres.in/img/faces/3-image.jpg"},
              {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos",
                  "avatar": "https://reqres.in/img/faces/6-image.jpg"})
    curr_method = request.method
    if curr_method == 'GET':
        if 'searchInput' in request.args:
            search = request.args['searchInput']
            return render_template('assignment9.html', search=search, users=users1)

    if curr_method == 'POST':
        username = request.form['nickname']
        session['logged_in'] = True
        session['username'] = username
    return render_template('assignment9.html', request_method=request.method, username=username)


@app.route('/logout', methods=['GET' , 'POST'])
def logout():
    session['logged_in'] = False
    session['username'] = ' '
    return redirect(url_for('assignment9_fun'))


if __name__ == '__main__':
    app.run(debug=True)