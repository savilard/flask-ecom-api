from flask_ecom_api import Product  # type: ignore
from flask_ecom_api.app import marshmallow


class ProductSchema(marshmallow.SQLAlchemySchema):
    """Product marshmallow schema."""

    class Meta:  # noqa: WPS306, D106
        model = Product
        ordered = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    description = marshmallow.auto_field()
    price = marshmallow.auto_field()
    published = marshmallow.auto_field()


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
