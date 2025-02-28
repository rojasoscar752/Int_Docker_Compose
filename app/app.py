# app.py
from flask import Flask, jsonify
from database import create_table, get_db_connection

app = Flask(__name__)

# Configura los parámetros de conexión a la base de datos
app.config['DB_HOST'] = 'db'
app.config['DB_PORT'] = '5432'
app.config['DB_NAME'] = 'mydatabase'
app.config['DB_USER'] = 'user'
app.config['DB_PASSWORD'] = 'password'

# Crear las tablas antes de la primera solicitud
@app.before_first_request
def init_db():
    create_table()

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM your_table_name;')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

