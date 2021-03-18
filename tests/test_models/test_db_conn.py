def test_db_create(test_database, test_product):
    test_database.session.add(test_product)
    test_database.session.commit()

    assert test_product.query.first()
