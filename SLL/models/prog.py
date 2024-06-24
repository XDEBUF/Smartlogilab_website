from SLL.extension import db, Base
class Prog(Base):
    __tablename__ = 'prog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    post_date = db.Column(db.DateTime)
    content = db.Column(db.Text)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    orientation = db.Column(db.Integer)