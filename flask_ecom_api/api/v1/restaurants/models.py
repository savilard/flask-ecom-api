from sqlalchemy_utils import PhoneNumberType

from flask_ecom_api import admin, db
from flask_ecom_api.api.v1.products.models import Product
from flask_ecom_api.api.v1.restaurants.admin import (
    CourierAdminView,
    RestaurantAdminView,
    RestaurantCourierAdminView,
    RestaurantProductAdminView,
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
    contact_phone = db.Column(PhoneNumberType())

    couriers = db.relationship('RestaurantCourier', lazy='joined', back_populates='restaurant')
    products = db.relationship('RestaurantProduct', lazy='joined', back_populates='restaurant')

    def __repr__(self):
        """Printable representation of Restaurant model."""
        return f'<Restaurant id: {self.id}>'


class Courier(db.Model):
    """Courier model."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    contact_phone = db.Column(PhoneNumberType(), nullable=False)
    vk_id = db.Column(db.String(25))
    tg_id = db.Column(db.String(25))
    fb_id = db.Column(db.String(25))

    def __repr__(self):
        """Return a printable representation of the Courier model."""
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
        """Printable representation of RestaurantCourier model."""
        return f'<RestaurantCourier restaurant: {self.restaurant_id} courier: {self.courier_id}>'


class RestaurantProduct(db.Model):
    """Restaurant product model."""

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey('restaurant.id'),
        index=True,
        nullable=False,
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        index=True,
        nullable=False,
    )
    availability = db.Column(db.Boolean)

    restaurant = db.relationship('Restaurant', lazy='joined')
    product = db.relationship(Product, lazy='joined')

    def __repr__(self):
        """Printable representation of RestaurantProduct model."""
        return f'<RestaurantProduct restaurant: {self.restaurant_id} product: {self.product_id}>'


admin.add_view(RestaurantAdminView(Restaurant, db.session, category='Restaurants'))
admin.add_view(CourierAdminView(Courier, db.session, category='Restaurants'))
admin.add_view(RestaurantCourierAdminView(RestaurantCourier, db.session, category='Restaurants'))
admin.add_view(RestaurantProductAdminView(RestaurantProduct, db.session, category='Restaurants'))
