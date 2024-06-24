from flask import request, redirect, url_for, render_template
from flask_login import current_user
from . import actu
from SLL.models.actu import Actu
from datetime import datetime
from SLL.file_service import save_on_server
from flask_login import  login_required
from SLL.extension import db


@actu.route("/actualites")
def actualite():
    blogs = db.session.query(Actu)
    article = blogs.order_by(Actu.post_date.desc()).all()
    print(current_user.is_anonymous)
    if current_user.is_anonymous:
        name = "guest"
    else:
        name = current_user.username
        print("bye")

    return render_template('actualites.html', article=article, name=name)

@actu.route('/addActu', methods=['POST', 'GET'])
@login_required
def addActu():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        file = request.files['file']
        file_name = save_on_server(file)
        orientation = request.form['orientation']
        post = Actu(title=title, author=author,
                    content=content, post_date=datetime.now(),
                    filename=file_name,
                    orientation=orientation
                    )
        db.session.add(post)
        print(post.title)
        db.session.commit()
        print("Done")
        return redirect(url_for('actu.actualite'))
    return render_template('addActu.html')

@actu.route('/updateActu/<int:id>', methods=['POST', 'GET'])
@login_required
def updateActu(id):
    blogs = db.session.query(Actu)
    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        file = request.files['file']
        file_name = save_on_server(file)

        post = blogs.filter_by(id=id).first()

        post.title = title
        post.author = author
        post.content = content
        post.filename = file_name

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('actu.actualite'))

    edit = blogs.filter_by(id=id).first()
    return render_template('updateActu.html', edit=edit)

@actu.route('/deleteActu/<int:id>')
@login_required
def deleteActu(id):
    blogs = db.session.query(Actu)
    d = blogs.filter_by(id=id).first()
    db.session.delete(d)
    db.session.commit()
    return redirect(url_for('actu.actualite'))