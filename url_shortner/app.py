from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random

app = Flask(__name__)

# 🔹 Create database
def init_db():
    conn = sqlite3.connect('urls.db')
    conn.execute('CREATE TABLE IF NOT EXISTS urls (short TEXT PRIMARY KEY, long TEXT)')
    conn.close()

init_db()

# 🔹 Generate short code
def generate_short():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

# 🔹 Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None

    if request.method == 'POST':
        long_url = request.form['long_url']

        while True:
           short = generate_short()
           conn = sqlite3.connect('urls.db')
           result = conn.execute('SELECT * FROM urls WHERE short=?', (short,)).fetchone()
           conn.close()
           if not result:
             break
        
        conn = sqlite3.connect('urls.db')
        conn.execute('INSERT INTO urls (short, long) VALUES (?, ?)', (short, long_url))
        conn.commit()
        conn.close()

        short_url = request.host_url + short

    return render_template('index.html', short_url=short_url)

# 🔹 Redirect route
@app.route('/<short>')
def redirect_url(short):
    conn = sqlite3.connect('urls.db')
    result = conn.execute('SELECT long FROM urls WHERE short=?', (short,)).fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "URL not found ❌"

if __name__ == '__main__':
    app.run(debug=True)