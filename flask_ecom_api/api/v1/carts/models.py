from datetime import datetime

from flask_ecom_api import db


class Cart(db.Model):
    """Cart model."""

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customer.id'),
        index=True,
        unique=True,
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)
    expires_at = db.Column(db.DateTime)
