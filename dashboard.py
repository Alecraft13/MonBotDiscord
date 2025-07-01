from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB = 'config.db'

@app.route('/')
def index():
    # Lire le message actuel dans la base
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT announcement_message FROM config WHERE id = 1')
    message = c.fetchone()[0]
    conn.close()
    return render_template('index.html', message=message)

@app.route('/update', methods=['POST'])
def update():
    # Mettre à jour le message dans la base
    new_message = request.form['message']
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('UPDATE config SET announcement_message = ? WHERE id = 1', (new_message,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

