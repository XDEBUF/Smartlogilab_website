from flask import render_template
from SLL.gouv import gouv

@gouv.route('/Membres')
def membres():
    return render_template('Membres.html')
@gouv.route('/Gouvernances')
def gouvernances():
    return render_template('gouvernances.html')
