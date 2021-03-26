from flask_ecom_api import db
from flask_ecom_api.api.v1.products.models import Product

restaurant_couriers = db.Table(
    'restaurant_couriers',
    db.Column(
        'restaurant_id',
        db.Integer,
        db.ForeignKey('restaurant.id'),
        primary_key=True,
    ),
    db.Column(
      'courier_id',
      db.Integer,
      db.ForeignKey('courier.id'),
      primary_key=True,
    ),
)

restaurant_products = db.Table(
    'restaurant_products',
    db.Column(
        'restaurant_id',
        db.Integer,
        db.ForeignKey('restaurant.id'),
        primary_key=True,
    ),
    db.Column(
        'product_id',
        db.Integer,
        db.ForeignKey('product.id'),
        primary_key=True,
    ),
    db.Column(
        'availability',
        db.Boolean,
    ),
)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        unique=True,
        nullable=False,
    )
    address = db.Column(db.String(length=140), index=True, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    contact_phone = db.Column(db.String(10))

    couriers = db.relationship(
        'Courier',
        secondary=restaurant_couriers,
        lazy='subquery',
        backref=db.backref('restaurants', lazy='joined'),
    )

    products = db.relationship(
        Product,
        secondary=restaurant_products,
        lazy='subquery',
        backref=db.backref('restaurants', lazy='joined'),
    )

    def __repr__(self):
        return f'<Restaurant id: {self.id}>'


class Courier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    contact_phone = db.Column(db.String(10), nullable=False)
    vk_id = db.Column(db.String(25))
    tg_id = db.Column(db.String(25))
    fb_id = db.Column(db.String(25))

    def __repr__(self):
        return f'<Courier id: {self.id}>'
