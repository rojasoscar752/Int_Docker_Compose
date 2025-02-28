# database.py
import psycopg2
from psycopg2 import sql
from flask import current_app

def get_db_connection():
    connection = psycopg2.connect(
        host=current_app.config['DB_HOST'],
        port=current_app.config['DB_PORT'],
        dbname=current_app.config['DB_NAME'],
        user=current_app.config['DB_USER'],
        password=current_app.config['DB_PASSWORD']
    )
    return connection

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS your_table_name (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(create_table_query)
    
    # Insertar datos iniciales si es necesario
    insert_data_query = "INSERT INTO your_table_name (name) VALUES (%s) ON CONFLICT (id) DO NOTHING;"
    cursor.execute(insert_data_query, ('Oscar Rojas',))
    cursor.execute(insert_data_query, ('Pepito Perez',))
    
    conn.commit()
    cursor.close()
    conn.close()
