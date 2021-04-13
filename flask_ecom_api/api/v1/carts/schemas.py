from flask_ecom_api import Cart, CartProduct  # type: ignore
from flask_ecom_api.app import marshmallow


class CartProductSchema(marshmallow.SQLAlchemySchema):
    """Cart product marshmallow schema."""

    class Meta:
        model = CartProduct
        ordered = True

    id = marshmallow.auto_field()
    cart_id = marshmallow.auto_field()
    restaurant_product_id = marshmallow.auto_field()
    quantity = marshmallow.auto_field()


class CartSchema(marshmallow.SQLAlchemySchema):
    """Cart marshmallow schema."""

    class Meta:
        model = Cart
        ordered = True

    id = marshmallow.auto_field()
    reference = marshmallow.auto_field()
    created_at = marshmallow.auto_field()
    updated_at = marshmallow.auto_field()
    expires_at = marshmallow.auto_field()


cart_schema = CartSchema()
cart_product_schema = CartProductSchema()
