import pytest

from flask_ecom_api import create_app, db


@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('flask_ecom_api.config.TestingConfig')
    with app.app_context():
        yield app


@pytest.fixture(scope='module')
def test_database(test_app):
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
