import pytest
from unittest.mock import patch
from main import app, get_data_from_db, process_data

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_data_from_db_returns_correct_data():
    mock_data = {'id': 1, 'name': 'Test Item'}
    with patch('main.get_data_from_db', return_value=mock_data):
        data = get_data_from_db()
        assert data == mock_data

def test_process_data_transforms_data_correctly():
    input_data = {'id': 1, 'name': 'Test Item'}
    expected_output = {'id': 1, 'name': 'TEST ITEM'}
    result = process_data(input_data)
    assert result == expected_output

def test_api_endpoint_returns_expected_data(client):
    mock_data = {'id': 1, 'name': 'Test Item'}
    with patch('main.get_data_from_db', return_value=mock_data):
        response = client.get('/api/data')
        assert response.status_code == 200
        assert response.json == mock_data

def test_404_error_for_invalid_endpoint(client):
    response = client.get('/invalid-endpoint')
    assert response.status_code == 404