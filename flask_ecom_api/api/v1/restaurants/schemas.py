from flask_ecom_api import Restaurant, RestaurantProduct  # type: ignore
from flask_ecom_api.app import marshmallow


class RestaurantProductSchema(marshmallow.SQLAlchemySchema):
    """Restaurant product marshmallow schema."""

    class Meta:
        model = RestaurantProduct
        order = True

    id = marshmallow.auto_field()
    restaurant_id = marshmallow.auto_field()
    product_id = marshmallow.auto_field()
    availability = marshmallow.auto_field()


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
restaurant_product_schema = RestaurantProductSchema()
