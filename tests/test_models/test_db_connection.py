from flask_ecom_api.models.product import Product


def test_db_create(test_database):
    product = Product(name='test_product')
    test_database.session.add(product)
    test_database.session.commit()

    assert Product.query.first()
