from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_host = 'database'  # This should match the service name defined in Docker Compose
db_user = 'root'
db_password = 'prabin123'
db_name = 'DB'

def connect_to_database():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route('/')
def hello():
    try:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(data=data)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
