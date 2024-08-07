from SLL.extension import db, Base
class Publi(Base):
    __tablename__ = 'publi'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    post_date = db.Column(db.DateTime)
    content = db.Column(db.Text)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    orientation = db.Column(db.Integer)
    text_link = db.Column(db.String(50))
    link = db.Column(db.String(300))