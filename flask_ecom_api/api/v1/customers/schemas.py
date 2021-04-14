from flask_ecom_api import Customer, CustomerShippingAddress  # type: ignore
from flask_ecom_api.app import marshmallow


class CustomerShippingAddressSchema(marshmallow.SQLAlchemySchema):
    """Customer shipping address marshmallow schema."""

    class Meta:
        model = CustomerShippingAddress
        ordered = True

    id = marshmallow.auto_field()
    customer_id = marshmallow.auto_field()
    first_name = marshmallow.auto_field()
    last_name = marshmallow.auto_field()
    phone_number = marshmallow.auto_field()
    country = marshmallow.auto_field()
    city = marshmallow.auto_field()
    street = marshmallow.auto_field()
    house_number = marshmallow.auto_field()
    apartment_number = marshmallow.auto_field()
    postcode = marshmallow.auto_field()
    comment = marshmallow.auto_field()


class CustomerSchema(marshmallow.SQLAlchemySchema):
    """Customer marshmallow schema."""

    class Meta:
        model = Customer
        ordered = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    date_of_birth = marshmallow.auto_field()
    email = marshmallow.auto_field()

    shipping_addresses = marshmallow.Nested(CustomerShippingAddressSchema, many=True)


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
customer_shipping_address = CustomerShippingAddressSchema()
