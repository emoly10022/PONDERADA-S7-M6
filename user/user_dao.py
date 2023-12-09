import mysql.connector
from user.user_model import UserModel

def create_connection():
    return mysql.connector.connect(
        host='ponderada-s7-m6.cnxoiuoiesei.us-east-1.rds.amazonaws.com',
        user='admin',
        password='EMELYinteli123',
        database='semana7'
    )

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()

def close_connection(conn):
    conn.close()
    
class UserDAO:
    
    def __init__(self):
        self.conn = create_connection()
        create_table(self.conn)
        
    def __del__(self):
        close_connection(self.conn)
        
    def create_user(self, user):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (user.name, user.email, user.password))
        self.conn.commit()
        
    def get_user_by_id(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user_data = cursor.fetchone()
        return UserModel(*user_data) if user_data else None
    
    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users')
        all_users_data = cursor.fetchall()
        return [UserModel(*user_data) for user_data in all_users_data]
    
    def delete_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        self.conn.commit()
        
    def update_user(self, user):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users
            SET name=%s, email=%s, password=%s
            WHERE id=%s
        ''', (user.name, user.email, user.password, user.id))
        self.conn.commit()