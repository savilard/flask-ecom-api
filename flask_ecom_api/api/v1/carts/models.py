from datetime import datetime

from flask_ecom_api import db
from flask_ecom_api.api.v1.restaurants.models import RestaurantProduct


class Cart(db.Model):
    """Cart model."""

    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(50), unique=True, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)
    expires_at = db.Column(db.DateTime)

    products = db.relationship('CartProduct', lazy='joined')

    def __repr__(self):
        return f'<Cart id: {self.id}, customer id: {self.customer_id}>'


class CartProduct(db.Model):
    """Cart product model."""

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(
        db.Integer,
        db.ForeignKey('cart.id'),
        index=True,
        nullable=False,
    )
    restaurant_product_id = db.Column(
        db.Integer,
        db.ForeignKey('restaurant_product.id'),
        index=True,
        nullable=False,
    )
    quantity = db.Column(db.Integer, default=0)

    cart = db.relationship('Cart', lazy='joined')
    restaurant_product = db.relationship(RestaurantProduct, lazy='joined')

    def __repr__(self):
        return f'<CartProduct id: {self.id}>'
