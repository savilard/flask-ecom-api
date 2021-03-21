import json


def test_get_products(test_app):
    client = test_app.test_client()
    response = client.get('/api/v1/products')
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'success' in data['status']


def test_get_product(test_app):
    client = test_app.test_client()
    response = client.get('/api/v1/products/1')
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'success' in data['status']
