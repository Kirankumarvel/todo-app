from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Database setup
def init_db():
    if not os.path.exists('tasks.db'):
        with sqlite3.connect('tasks.db') as conn:
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

# Initialize the database on app startup
init_db()

# Helper function to get a database connection
def get_db_connection():
    return sqlite3.connect('tasks.db')

# Route to display all tasks
@app.route('/')
def index():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM tasks')
            tasks = c.fetchall()
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        flash(f"Error fetching tasks: {e}", "error")
        return render_template('index.html', tasks=[])

# Route to add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name', '').strip()
        description = request.form.get('description', '').strip()

        if not task_name:
            flash("Task name is required", "error")
            return render_template('add_task.html')

        try:
            with get_db_connection() as conn:
                c = conn.cursor()
                c.execute('INSERT INTO tasks (task_name, description) VALUES (?, ?)', (task_name, description))
                conn.commit()
            flash("Task added successfully!", "success")
            return redirect('/')
        except Exception as e:
            flash(f"Error adding task: {e}", "error")
            return render_template('add_task.html')

    return render_template('add_task.html')

# Route to update an existing task
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    if request.method == 'POST':
        task_name = request.form.get('task_name', '').strip()
        description = request.form.get('description', '').strip()

        if not task_name:
            flash("Task name is required", "error")
            return redirect(f'/update/{id}')

        try:
            with get_db_connection() as conn:
                c = conn.cursor()
                c.execute(
                    'UPDATE tasks SET task_name=?, description=?, updated_at=CURRENT_TIMESTAMP WHERE id=?', 
                    (task_name, description, id)
                )
                conn.commit()
            flash("Task updated successfully!", "success")
            return redirect('/')
        except Exception as e:
            flash(f"Error updating task: {e}", "error")
            return redirect(f'/update/{id}')

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM tasks WHERE id=?', (id,))
            task = c.fetchone()
        if not task:
            flash(f"Task with id {id} not found", "error")
            return redirect('/')
        return render_template('update_task.html', task=task)
    except Exception as e:
        flash(f"Error fetching task: {e}", "error")
        return redirect('/')

# Route to delete a task
@app.route('/delete/<int:id>')
def delete_task(id):
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute('DELETE FROM tasks WHERE id=?', (id,))
            conn.commit()
        flash("Task deleted successfully!", "success")
    except Exception as e:
        flash(f"Error deleting task: {e}", "error")
    return redirect('/')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
