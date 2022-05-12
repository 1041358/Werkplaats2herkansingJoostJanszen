import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hT2oSIfqNzti%#QHNufpi3JFbAXe2XGCw5X0!EDxcbu!Q5L1@l'


def get_db_connection():
    conn = sqlite3.connect('scores.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['title']
        score = request.form['content']

        if not name:
            flash('Vul je naam in!')
        elif not score:
            flash('Vul je score in!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO highscores (name, score) VALUES (?, ?)',
                         (name, score))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/')
def index():
    conn = get_db_connection()
    highscores = conn.execute('SELECT * FROM highscores order by score DESC limit 10').fetchall()
    conn.close()
    return render_template('index.html', highscores=highscores)