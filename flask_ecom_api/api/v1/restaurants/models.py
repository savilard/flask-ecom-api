from flask_ecom_api import db


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

    restaurant_couriers = db.relationship(
        'Courier',
        secondary=restaurant_couriers,
        lazy='subquery',
        backref=db.backref('restaurants', lazy='joined'),
    )


class Courier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    contact_phone = db.Column(db.String(10), nullable=False)
    vk_id = db.Column(db.Integer)
    tg_id = db.Column(db.Integer)
    fb_id = db.Column(db.Integer)
