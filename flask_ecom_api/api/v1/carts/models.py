from datetime import datetime

from flask_ecom_api.api.v1.restaurants.models import RestaurantProduct
from flask_ecom_api.app import db


class Cart(db.Model):
    """Cart model."""

    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(50), unique=True, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)
    expires_at = db.Column(db.DateTime)

    products = db.relationship('CartProduct', lazy='joined', back_populates='cart')

    def total_amount(self):
        """Calculate cart total amount."""
        query = Cart.query.join(
            Cart.products,
            RestaurantProduct.product,
        ).filter(Cart.reference == self.reference).first()

        return sum(
            (
                product.restaurant_product.product.price * product.quantity
                for product in query.products
                if product.restaurant_product.availability
            ),
        )

    def __repr__(self):
        """Printable representation of Cart model."""
        return f'<Cart id: {self.id}, reference: {self.reference}>'


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

    __table_args__ = (  # type: ignore
        db.CheckConstraint(quantity >= 0, name='check_cart_product_quantity_non_negative'),
        {},
    )

    def __repr__(self):
        """Printable representation of CartProduct model."""
        return f'<CartProduct id: {self.id}>'
