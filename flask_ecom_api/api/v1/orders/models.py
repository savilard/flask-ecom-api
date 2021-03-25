import enum
from datetime import datetime

from flask_ecom_api import db
from flask_ecom_api.api.v1.products.models import Product

order_products = db.Table(
    'order_products',
    db.Column(
        'order_id',
        db.Integer,
        db.ForeignKey('order.id'),
        primary_key=True,
    ),
    db.Column(
        'product_id',
        db.Integer,
        db.ForeignKey('product.id'),
        primary_key=True,
    ),
    db.Column(
        'quantity',
        db.Integer,
    ),
    db.Column(
        'cost',
        db.DECIMAL(10, 2),
        default=0,
    ),
)


class OrderStatusEnum(enum.Enum):
    processed = 'processed'
    unprocessed = 'unprocessed'


class PaymentMethodEnum(enum.Enum):
    cash = 'cash'
    card = 'card'


class Order(db.Model):
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

    products = db.relationship(
        Product,
        secondary=order_products,
        lazy='subquery',
        backref=db.backref('orders', lazy='joined'),
    )
