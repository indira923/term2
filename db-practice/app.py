from time import time
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

from requests import post
# import time
# from requests import post

app = Flask(__name__)

@app.route('/')
def index():
    posts = get_all_posts ()

    return render_template('index.html', posts = posts)

@app.route('/success', methods=['POST'])
def submit():
    name = request.form['name']
    time = (request.form['time']) 
    post = request.form['posts']
    add_post(name, time, post)
  
    return render_template('success.html')

@app.route('/delete-post/<rowid>')
def delete(rowid):
    delete_post(rowid)
    return redirect(url_for('index'))


def delete_post(rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM Posts WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

@app.route('/edit-post/<rowid>', methods=['POST'])
def editpost(rowid):
    name = request.form['name']
    time = (request.form['time']) 
    post = request.form['post']
    update_post(name, time, post, rowid)

    return redirect(url_for('index'))


def update_post(name, time, post, rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("UPDATE Posts name = ?, time = ?, post = ?, WHERE rowid = ?", (name, time, post, rowid))
    conn.commit()
    conn.close()


def add_post(name, time, post):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO Posts (name, time, post) VALUES (?, ?, ?)", (name, time, post))
    conn.commit()
    conn.close()

def get_all_posts():
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM posts")
    posts = []

    for row in result: 
        post = {
            'name': row[1],
            'time': row[2],
            'post': row[3],
            'rowid' : row[0]

        }
        posts.append(post)

    conn.close()
    return posts

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')