from slugify import slugify

from flask_ecom_api import db

product_ingredients = db.Table(
    'product_ingredients',
    db.Column(
        'product_id',
        db.Integer,
        db.ForeignKey('product.id'),
        primary_key=True,
    ),
    db.Column(
        'ingredient_id',
        db.Integer,
        db.ForeignKey('ingredient.id'),
        primary_key=True,
    ),
)


product_categories = db.Table(
    'product_categories',
    db.Column(
        'product_id',
        db.Integer,
        db.ForeignKey('product.id'),
        primary_key=True,
    ),
    db.Column(
        'category_id',
        db.Integer,
        db.ForeignKey('category.id'),
        primary_key=True,
    ),
)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        unique=True,
        nullable=False,
    )
    slug = db.Column(db.String(length=140), unique=True, nullable=False)
    description = db.Column(db.Text)
    images = db.relationship('ProductImage', backref='product', lazy='joined')
    price = db.Column(db.DECIMAL(10, 2), default=0)
    published = db.Column(db.Boolean, default=False)

    ingredients = db.relationship(
        'Ingredient',
        secondary=product_ingredients,
        lazy='subquery',
        backref=db.backref('products', lazy='joined'),
    )

    categories = db.relationship(
        'Category',
        secondary=product_categories,
        lazy='subquery',
        backref=db.backref('products', lazy='joined'),
    )

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(text=self.name, max_length=140)

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


class Category(db.Model):
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
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(text=self.name, max_length=140)

    def __repr__(self):
        return f'<Category id: {self.id}, category name: {self.name}>'
