import pytest

from flask_ecom_api import app


@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('flask_ecom_api.config.TestingConfig')
    with app.app_context():
        yield app
