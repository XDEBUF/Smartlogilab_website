import SLL.models.user
from . import auth
from flask import  flash, request, redirect, url_for, render_template
from flask_login import  login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from SLL.models.user import User
from SLL.extension import db , login_manager

@login_manager.user_loader
def load_user(user_id):
    users = db.session.query(User)
    return users.get(int(user_id))
@auth.route('/login', methods=['POST', 'GET'])
def login():
    users = db.session.query(User)
    if request.method == 'POST':
        # print("hello")
        username = request.form['username']
        password = request.form['password']
        user = users.filter_by(username=username).first()

        if not user and not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            # return redirect(url_for('auth.login'))
            return render_template('index.html')
        else:
            login_user(user)
            print("yes")
            return redirect(url_for('index.index'))

    return render_template('login.html')


@auth.route('/signin', methods=['POST', 'GET'])
@login_required
def signin():
    if request.method == 'POST':
        print("hello")
        username = request.form['username']
        password = request.form['password']

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index.index'))

    return render_template('signin.html')


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))
