from flask_ecom_api import Customer  # type: ignore
from flask_ecom_api.app import marshmallow


class CustomerSchema(marshmallow.SQLAlchemySchema):
    """Customer marshmallow schema."""

    class Meta:
        model = Customer
        ordered = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    date_of_birth = marshmallow.auto_field()
    email = marshmallow.auto_field()


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
