from ai_site import db


def __init__():
    return Partner


class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Partner('{self.name}', '{self.description}')"