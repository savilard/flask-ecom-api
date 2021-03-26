from flask_ecom_api import db


class Customer(db.Model):
    """Customer model."""

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

    shipping_addresses = db.relationship('CustomerShippingAddress', backref='customer', lazy='joined')

    def __repr__(self):
        return f'<Customer id: {self.id}, customer name: {self.name}>'


class CustomerShippingAddress(db.Model):
    """Customer shipping address model."""

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customer.id'),
        index=True,
        nullable=False,
    )
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(140))

    def __repr__(self):
        return f'<Customer shipping address id: {self.id}>'
