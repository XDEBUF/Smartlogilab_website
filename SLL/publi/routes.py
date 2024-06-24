
from flask_login import login_required, current_user
from flask import request, redirect, url_for, render_template
from datetime import datetime
from . import publi
from SLL.models.publi import Publi
from SLL.file_service import save_on_server
from SLL.extension import db
@publi.route("/publications")
def publication():
    blogs = db.session.query(Publi)
    article = blogs.order_by(Publi.post_date.desc()).all()
    print(current_user.is_anonymous)
    if current_user.is_anonymous:
        name = "guest"
    else:
        name = current_user.username
        print("bye")

    return render_template('publications.html', article=article, name=name)
@publi.route('/addPub', methods=['POST', 'GET'])
@login_required
def addPub():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        file = request.files['file']
        file_name = save_on_server(file)
        orientation = request.form['orientation']
        text_link = request.form['text_link']
        link = request.form['link']
        post = Publi(title=title, author=author,
                    content=content, post_date=datetime.now(),
                    filename=file_name,
                    orientation=orientation,
                    text_link=text_link, link=link
                    )

        db.session.add(post)
        db.session.commit()
        print("Done")
        return redirect(url_for('publi.publication'))
    return render_template('addPub.html')
@publi.route('/updatePubli/<int:id>', methods=['POST', 'GET'])
@login_required
def updatePubli(id):
    blogs = db.session.query(Publi)
    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        file = request.files['file']
        file_name = save_on_server(file)
        link = request.form['link']
        text = request.form['text_link']
        post = blogs.filter_by(id=id).first()

        post.title = title
        post.author = author
        post.content = content
        post.filename = file_name
        post.text_link = text
        post.link = link

        db.session.add(post)
        db.session.commit()
        return redirect(url_for("publi.publication"))

    edit = blogs.filter_by(id=id).first()
    return render_template('updatePubli.html', edit=edit)