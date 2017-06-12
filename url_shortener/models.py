from url_shortener import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(length=300))
    short_url = db.Column(db.String(length=300))
