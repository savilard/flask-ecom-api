import enum
from datetime import datetime

from flask_ecom_api import db
from flask_ecom_api.api.v1.products.models import Product


class OrderStatusEnum(enum.Enum):
    """Class for choosing order statuses."""

    processed = 'processed'
    unprocessed = 'unprocessed'


class PaymentMethodEnum(enum.Enum):
    """Class for choosing payment methods."""

    cash = 'cash'
    card = 'card'


class Order(db.Model):
    """Order model."""

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(
        db.Enum(OrderStatusEnum),
        default=OrderStatusEnum.unprocessed,
        nullable=False,
    )
    payment_method = db.Column(
        db.Enum(PaymentMethodEnum),
        default=PaymentMethodEnum.cash,
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    delivered_at = db.Column(db.DateTime)
    comment = db.Column(db.Text)

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customer.id'),
        index=True,
        nullable=False,
    )

    customer = db.relationship('Customer', lazy='joined')
    products = db.relationship('OrderProduct', lazy='joined')

    def __repr__(self):
        return f'<Order id: {self.id}, order name: {self.name}>'


class OrderProduct(db.Model):
    """Order product model."""

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey('order.id'),
        index=True,
        nullable=False,
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        index=True,
        nullable=False,
    )
    quantity = db.Column(db.Integer, default=0)
    cost = db.Column(db.DECIMAL(10, 2), default=0)

    order = db.relationship('Order', lazy='joined')
    product = db.relationship(Product, lazy='joined')

    __table_args__ = (
        db.CheckConstraint(
            quantity >= 0,
            name='check_order_product_quantity_non_negative',
        ),
        {},
    )

    def __repr__(self):
        return f'<OrderProduct order: {self.order_id} product: {self.product_id}>'
