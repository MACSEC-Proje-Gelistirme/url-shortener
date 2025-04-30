from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URL(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    root_url = db.Column(db.String(120), unique=False, nullable=False)
    child_url = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    shortened_url = db.Column(db.String(80), unique=True, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'root_url': self.root_url,
            'child_url': self.child_url,
            'url': self.url,
            'shortened_url': self.shortened_url
        }