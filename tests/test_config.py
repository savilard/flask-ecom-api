import os


def test_development_config(test_app):
    test_app.config.from_object('flask_ecom_api.config.DevelopmentConfig')
    assert not test_app.config['TESTING']


def test_testing_config(test_app):
    test_app.config.from_object('flask_ecom_api.config.TestingConfig')
    assert test_app.config['TESTING']


def test_production_config(test_app):
    test_app.config.from_object('flask_ecom_api.config.ProductionConfig')
    assert not test_app.config['TESTING']
