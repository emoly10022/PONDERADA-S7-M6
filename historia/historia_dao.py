import mysql.connector
from historia.historia_model import HistoriaModel

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
        CREATE TABLE IF NOT EXISTS historia (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT
        )
    ''')
    conn.commit()

def close_connection(conn):
    conn.close()  
    
class HistoriaDAO:
    
    def __init__(self):
        self.conn = create_connection()
        create_table(self.conn)
        
    def __del__(self):
        close_connection(self.conn)
        
    def create_historia(self, historia: HistoriaModel):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO historia (content) VALUES (%s)', (historia.content,))
        self.conn.commit()
        historia.id = cursor.lastrowid
        
    def get_historia_by_id(self, historia_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM historia WHERE id = %s', (historia_id,))
        historia_data = cursor.fetchone()
        return HistoriaModel(*historia_data) if historia_data else None
    
    def get_all_historias(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM historia')
        all_historias_data = cursor.fetchall()
        return [HistoriaModel(*historia_data) for historia_data in all_historias_data]
    
    def delete_historia(self, historia_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM historia WHERE id = %s', (historia_id,))
        self.conn.commit()
        
    def update_historia(self, historia: HistoriaModel):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE historia
            SET content = %s
            WHERE id = %s
        ''', (historia.content, historia.id))
        self.conn.commit()
        
