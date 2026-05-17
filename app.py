from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create Database Table
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')

conn.commit()
conn.close()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Contact Form
@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    return "Message Saved Successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)