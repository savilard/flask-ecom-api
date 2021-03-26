from flask_ecom_api import db
from flask_ecom_api.api.v1.products.models import Product


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
    """Restaurant model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        nullable=False,
    )
    address = db.Column(db.String(length=140), index=True, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    contact_phone = db.Column(db.String(10))

    couriers = db.relationship('RestaurantCourier')

    products = db.relationship(
        Product,
        secondary=restaurant_products,
        lazy='subquery',
        backref=db.backref('restaurants', lazy='joined'),
    )

    def __repr__(self):
        return f'<Restaurant id: {self.id}>'


class Courier(db.Model):
    """Courier model."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    contact_phone = db.Column(db.String(10), nullable=False)
    vk_id = db.Column(db.String(25))
    tg_id = db.Column(db.String(25))
    fb_id = db.Column(db.String(25))

    def __repr__(self):
        """Return a printable representation of the courier class."""
        return f'<Courier id: {self.id}>'


class RestaurantCourier(db.Model):
    """Restaurant сourier model."""

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey('restaurant.id'),
        index=True,
        nullable=False,
    )
    courier_id = db.Column(
        db.Integer,
        db.ForeignKey('courier.id'),
        index=True,
        nullable=False,
    )
    restaurant = db.relationship('Restaurant', lazy='joined')
    courier = db.relationship('Courier', lazy='joined')

    def __repr__(self):
        return f'<RestaurantCourier restaurant: {self.restaurant_id} courier: {self.courier_id}>'
