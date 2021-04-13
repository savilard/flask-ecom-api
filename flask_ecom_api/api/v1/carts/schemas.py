from flask_ecom_api import Cart  # type: ignore
from flask_ecom_api.app import marshmallow


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
