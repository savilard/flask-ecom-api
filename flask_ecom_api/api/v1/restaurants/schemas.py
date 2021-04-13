from flask_ecom_api import Restaurant  # type: ignore
from flask_ecom_api.app import marshmallow


class RestaurantSchema(marshmallow.SQLAlchemySchema):
    """Restaurant marshmallow schema."""

    class Meta:
        model = Restaurant
        order = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    address = marshmallow.auto_field()
    latitude = marshmallow.auto_field()
    longitude = marshmallow.auto_field()
    contact_phone = marshmallow.auto_field()


restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)
