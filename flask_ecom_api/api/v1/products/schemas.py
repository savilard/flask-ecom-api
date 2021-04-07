from flask_ecom_api import (  # type: ignore
    Category,
    Ingredient,
    Product,
    ProductImage,
)
from flask_ecom_api.app import marshmallow


class IngredientSchema(marshmallow.SQLAlchemySchema):
    """Product ingredient schema."""

    class Meta:
        model = Ingredient
        ordered = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    image_src = marshmallow.auto_field()
    weight = marshmallow.auto_field()
    price = marshmallow.auto_field()


class ProductImageSchema(marshmallow.SQLAlchemySchema):
    """Product image marshmallow schema."""

    class Meta:
        model = ProductImage
        ordered = True

    id = marshmallow.auto_field()
    src = marshmallow.auto_field()
    product_id = marshmallow.auto_field()
    is_main = marshmallow.auto_field()


class CategorySchema(marshmallow.SQLAlchemySchema):
    """Product category marshmallow schema."""

    class Meta:
        model = Category
        ordered = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    description = marshmallow.auto_field()
    parent_id = marshmallow.auto_field()


class ProductSchema(marshmallow.SQLAlchemySchema):
    """Product marshmallow schema."""

    class Meta:
        model = Product
        ordered = True

    id = marshmallow.auto_field()
    name = marshmallow.auto_field()
    description = marshmallow.auto_field()
    price = marshmallow.auto_field()
    published = marshmallow.auto_field()
    ingredients = marshmallow.Nested(IngredientSchema, many=True)
    images = marshmallow.Nested(ProductImageSchema, many=True)
    categories = marshmallow.Nested(CategorySchema, many=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
