from slugify import slugify

from flask_ecom_api import db


class Product(db.Model):
    """Product model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=140), index=True, nullable=False)
    slug = db.Column(db.String(length=140), nullable=False)
    description = db.Column(db.Text)
    images = db.relationship('ProductImage', backref='product', lazy='joined')
    price = db.Column(db.DECIMAL(10, 2), default=0)
    published = db.Column(db.Boolean, default=False)

    ingredients = db.relationship('ProductIngredient')
    categories = db.relationship('ProductCategory')

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        """Generate slug for product."""
        if self.name:
            self.slug = '{product_id}-{slug}'.format(
                product_id=self.id,
                slug=slugify(text=self.name, max_length=140),
            )

    def __repr__(self):
        return f'<Product id: {self.id}, product name: {self.name}>'


class ProductImage(db.Model):
    """Model for product images."""

    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(140), nullable=False)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        index=True,
        nullable=False,
    )
    is_main = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Image id: {self.id}, image src: {self.src}>'


class Ingredient(db.Model):
    """Model for product ingredient."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        unique=True,
        nullable=False,
    )
    image_src = db.Column(db.String(140))
    weight = db.Column(db.Integer, default=0)
    price = db.Column(db.DECIMAL(10, 2), default=0)

    def __repr__(self):
        return f'<Ingredient id: {self.id}, ingredient name: {self.name}>'


class ProductIngredient(db.Model):
    """Product ingredients model."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        index=True,
        nullable=False,
    )
    ingredient_id = db.Column(
        db.Integer,
        db.ForeignKey('ingredient.id'),
        index=True,
        nullable=False,
    )
    product = db.relationship('Product', lazy='joined')
    ingredient = db.relationship('Ingredient', lazy='joined')


class Category(db.Model):
    """Model for product category."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        unique=True,
        nullable=False,
    )
    slug = db.Column(db.String(length=140), unique=True, nullable=False)
    description = db.Column(db.Text)

    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    parent = db.relationship('Category', remote_side=id, backref='subcategories')

    def __init__(self, *args, **kwargs):
        """Init of category class."""
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        """Generate slug for category."""
        if self.name:
            self.slug = slugify(text=self.name, max_length=140)

    def __repr__(self):
        return f'<Category id: {self.id}, category name: {self.name}>'


class ProductCategory(db.Model):
    """Product categories model."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        index=True,
        nullable=False,
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        index=True,
        nullable=False,
    )
    product = db.relationship('Product', lazy='joined')
    category = db.relationship('Category', lazy='joined')
