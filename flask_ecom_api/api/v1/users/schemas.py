from flask_ecom_api import User  # type: ignore
from flask_ecom_api.app import marshmallow


class UserSchema(marshmallow.SQLAlchemySchema):
    """User marshmallow schema."""

    class Meta:
        model = User
        ordered = True

    id = marshmallow.auto_field()
    username = marshmallow.auto_field()
    email = marshmallow.auto_field()
    password = marshmallow.auto_field()
    active = marshmallow.auto_field()
    created_date = marshmallow.auto_field()


user_schema = UserSchema()
custom_user_schema = UserSchema(only=('email',))
