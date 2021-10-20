from flask import render_template
from app import app, db
from app.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    list_user = db.session.execute('SELECT * FROM User join Post on User.id = Post.user_id')
    return render_template('index.html', title='Homepage',luser=list_user)