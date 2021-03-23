from slugify import slugify

from flask_ecom_api import db


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
