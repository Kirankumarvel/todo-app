from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'incomplete'
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database on app startup
init_db()

# Route to display all tasks
@app.route('/')
def index():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        description = request.form['description']
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('INSERT INTO tasks (task_name, description) VALUES (?, ?)', (task_name, description))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_task.html')

# Route to update an existing task
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    if request.method == 'POST':
        task_name = request.form['task_name']
        description = request.form['description']
        c.execute('UPDATE tasks SET task_name=?, description=?, updated_at=CURRENT_TIMESTAMP WHERE id=?', 
                  (task_name, description, id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    c.execute('SELECT * FROM tasks WHERE id=?', (id,))
    task = c.fetchone()
    conn.close()
    return render_template('update_task.html', task=task)

# Route to delete a task
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
