def test_get_products(test_app):
    client = test_app.test_client()
    response = client.get('/api/v1/products')
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'success' in json_data['status']


def test_get_product(test_app):
    client = test_app.test_client()
    response = client.get('/api/v1/products/1')
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'success' in json_data['status']
