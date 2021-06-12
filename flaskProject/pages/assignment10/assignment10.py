from flask import redirect, request, Blueprint, render_template
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', passwd='amit1993', database='amitsql', auth_plugin='mysql_native_password')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statement
        # returns: the number of rows affected by query
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10')
@assignment10.route('/users')
def users():
    query = "select * from amitsql.users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insertion', methods=['GET', 'POST'])
def insertion():
    if request.method == 'POST':
        id_number = request.form['id']
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        avatar = request.form['avatar']
        query = "INSERT into amitsql.users (id, email, first_name, last_name, avatar) VALUES ('%s', '%s', '%s', '%s','%s')" % (id_number, email, first_name, last_name, avatar)
        interact_db(query, 'commit')
    return redirect('/assignment10')


@assignment10.route('/Deletion', methods=['GET', 'POST'])
def Deletion():
    if request.method == 'POST':
        id_number = request.form['id']
        query = "DELETE FROM amitsql.users WHERE id='%s';" % id_number
        interact_db(query, 'commit')
        return redirect('/assignment10')


@assignment10.route('/updating')
def updating():
    id_number = request.args['id']
    email = request.args['email']
    query = "UPDATE amitsql.users SET email = '%s' WHERE id = '%s' " % (email, id_number)
    interact_db(query, query_type='commit')
    return redirect('/assignment10')