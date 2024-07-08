
from flask_login import login_required, current_user
from flask import request, redirect, url_for, render_template,Response
from datetime import datetime
from . import publi
from SLL.models.Publi_selected import Publi_selected
from SLL.file_service import save_on_server
from SLL.extension import db
from .HAL_Search import json_HAL
import numpy as np
@publi.route("/publications")
def publication():
    blogs = db.session.query(Publi_selected)
    article = blogs.order_by(Publi_selected.post_date.desc()).all()

    print(current_user.is_anonymous)
    if current_user.is_anonymous:
        name = "guest"
    else:
        name = current_user.username
        print("bye")

    return Response(render_template('publications.html',  name=name, article=article))

@publi.route('/addPub', methods=['POST', 'GET'])
@login_required
def addPub():
    hal_articles=[]
    author_db=''
    if request.method == 'POST':
        author = request.form['author']
        ''' faire une regex pour selectionner les uniquement les carecteres (min ou maj) et les mettre en min puis séparer par une virgule '''
        author = author.strip()
        author = author.replace(' ', ',')
        author = author.lower()
        author_db = str(author)
        print('author', type(author))
        print('author_db', author_db)
        author = np.array([author], dtype="object")
        hal_articles = json_HAL(author)
        values = request.form.getlist('article_select')
        for value in values:
            post = Publi_selected( publication=value, post_date=datetime.now())
            db.session.add(post)
        db.session.commit()
    return render_template('addPub.html', hal_articles=hal_articles)

@publi.route('/deletePubli/<int:id>')
@login_required
def deletePubli(id):
    blogs = db.session.query(Publi_selected)
    d = blogs.filter_by(id=id).first()
    db.session.delete(d)
    db.session.commit()
    return redirect(url_for('publi.publication'))

