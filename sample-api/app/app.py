
from flask import Flask, jsonify, request
from  flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'softdevP'

mysql = MySQL(app)

@app.route('/')
def index():
    return "Index!"

@app.route('/user', methods=['GET'])
def get_data():
    cur =  mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/user/new', methods=['POST'])
def new_user():
    cur =  mysql.connection.cursor()
    id = request.json['id']
    name = request.json['name']
    age = request.json['age']
    cur.execute('''INSERT INTO users VALUES (%s, %s, %s)''', (id, name, age))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'create success'})


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    cur = mysql.connection.cursor()
    name = request.json['name']
    age = request.json['age']
    cur.execute('''UPDATE users SET name=%s, age=%s WHERE uid=%s''', (name, age, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'update success'})

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users WHERE uid=%s''', (id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('''DELETE FROM users WHERE id=%s''', (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'status': 'delete success'})
    except Exception as e:
        return jsonify({'status': 'delete fail', 'error': str(e)})

if __name__ == '__main__':
    app.run()