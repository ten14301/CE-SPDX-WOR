from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DB889'
app.config['MYSQL_DB'] = 'softdevP'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/')
def index():
    return "Index!"

@app.route('/user', methods=['GET'])
def get_data():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users')
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/user/new', methods=['POST'])
def new_user():
    try:
        cur = mysql.connection.cursor()
        username = request.json['username']
        email = request.json['email']
        cur.execute('INSERT INTO users (username, email) VALUES (%s, %s)', (username, email))
        mysql.connection.commit()
        cur.close()
        return jsonify({'status': 'create success'})
    except Exception as e:
        return jsonify({'status': 'create fail', 'error': str(e)})

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        cur = mysql.connection.cursor()
        username = request.json['username']
        email = request.json['email']
        cur.execute('UPDATE users SET username=%s, email=%s WHERE id=%s', (username, email, id))
        mysql.connection.commit()
        cur.close()
        return jsonify({'status': 'update success'})
    except Exception as e:
        return jsonify({'status': 'update fail', 'error': str(e)})

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id=%s', (id,))
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM users WHERE id=%s', (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'status': 'delete success'})
    except Exception as e:
        return jsonify({'status': 'delete fail', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
