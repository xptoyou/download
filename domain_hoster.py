from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('domains.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS domains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT UNIQUE
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_domain', methods=['POST'])
def check_domain():
    domain = request.form['domain']
    with sqlite3.connect('domains.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM domains WHERE domain = ?', (domain,))
        result = cursor.fetchone()
        if result:
            return jsonify({'available': False, 'message': 'Domain is already taken.'})
        else:
            return jsonify({'available': True, 'message': 'Domain is available.'})

@app.route('/register_domain', methods=['POST'])
def register_domain():
    domain = request.form['domain']
    with sqlite3.connect('domains.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO domains (domain) VALUES (?)', (domain,))
            conn.commit()
            return jsonify({'success': True, 'message': f'Domain {domain} registered successfully!'})
        except sqlite3.IntegrityError:
            return jsonify({'success': False, 'message': 'Domain is already registered.'})

if __name__ == '__main__':
    app.run(debug=True)
