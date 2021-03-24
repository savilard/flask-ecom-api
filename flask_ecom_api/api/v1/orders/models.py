import enum
from datetime import datetime

from flask_ecom_api import db


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
