from flask_ecom_api import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=50),
        index=True,
        unique=True,
        nullable=False,
    )
    date_of_birth = db.Column(db.DateTime)
    email = db.Column(
        db.String(length=50),
        index=True,
        unique=True,
        nullable=False,
    )

    def __repr__(self):
        return f'<Customer id: {self.id}, customer name: {self.name}>'
