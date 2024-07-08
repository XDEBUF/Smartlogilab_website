from . import prog
from flask import request, redirect, url_for, render_template
from flask_login import login_required, current_user
from SLL.models.prog import Prog
from datetime import datetime

from SLL.file_service import save_on_server
from SLL.extension import db
@prog.route("/programmes")
def programme():
    blogs = db.session.query(Prog)
    article = blogs.order_by(Prog.post_date).all()
    print(current_user.is_anonymous)
    if current_user.is_anonymous:
        name = "guest"
    else:
        name = current_user.username
        print("bye")

    return render_template('programmes.html', article=article, name=name)

@prog.route('/addProg', methods=['POST', 'GET'])
@login_required
def addProg():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        file = request.files['file']
        file_name = save_on_server(file)
        orientation = request.form['orientation']
        post = Prog(title=title, author=author,
                    content=content, post_date=datetime.now(),
                    filename=file_name,
                    orientation=orientation)
        db.session.add(post)
        db.session.commit()
        print("Done")
        return redirect(url_for('prog.programme'))
    return render_template('addProg.html')
@prog.route('/updateProg/<int:id>', methods=['POST', 'GET'])
@login_required
def updateProg(id):
    blog = db.session.query(Prog)
    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        file = request.files['file']
        file_name = save_on_server(file)
        post = blog.filter_by(id=id).first()

        post.title = title
        post.author = author
        post.content = content
        if file_name:
            post.filename = file_name

        db.session.add(post)
        db.session.commit()
        return redirect(url_for("prog.programme"))

    edit = blog.filter_by(id=id).first()
    return render_template('updateProg.html', edit=edit)

@prog.route('/deleteProg/<int:id>')
@login_required
def deleteProg(id):
    blogs = db.session.query(Prog)
    d = blogs.filter_by(id=id).first()
    db.session.delete(d)
    db.session.commit()
    return redirect(url_for('prog.programme'))