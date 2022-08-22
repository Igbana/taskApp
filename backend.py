from datetime import date, timedelta
import sqlite3

conn = sqlite3.connect('main.db')
cur = conn.cursor()

class Database:
    def __init__(self):
        cur.execute('CREATE TABLE IF NOT EXISTS tasks (task_name, date_created)')
        cur.execute('DELETE from tasks WHERE date_created = ?', [str(date.today() - timedelta(days=1))])
        conn.commit()
        
    def get_tasks(self):
        tasks = []
        cur.execute('SELECT task_name from tasks WHERE date_created = ?', [str(date.today())])
        for item in cur.fetchall():
            tasks.append(item[0])
        return tasks
    
    def add_task(self, task):
        cur.execute('INSERT INTO tasks VALUES (?, ?)', [task, str(date.today())])
        conn.commit()

    def delete_task(self, task):
        cur.execute('DELETE from tasks WHERE task_name = ?', [task])
        conn.commit()