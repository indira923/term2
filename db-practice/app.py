from flask import Flask, render_template, request
import sqlite3
import time
from requests import post

app = Flask(__name__)

@app.route('/')
def index():
    user_post = user_post()

    return render_template('index.html', posts = post)

@app.route('/success', methods=['POST'])
def submit():
    name = request.form['name']
    time = int(request.form['time']) 
    # height = request.form['height']
    # group = request.form['group']
    add_post(name, time, post, )
  
    return render_template('success.html')

def add_post(name, time, post,):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO write_post (name, time, post) VALUES (?, ?, ?)", (name, time, post, ))
    conn.commit()
    conn.close()

def get_all_posts():
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM posts")
    posts = []

    for row in result: 
        post = {
            'name': row[0],
            'time': row[1],
            'post': row[2],

        }
        posts.append(post)

    conn.close()
    return posts

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')