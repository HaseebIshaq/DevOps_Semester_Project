import pytest
from app import app

# Create a test client for the Flask application
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the index route
def test_index(client):
    # Send a GET request to the index route
    response = client.get('/')
    
    # Check if the response contains the expected text in the page
    assert b'Student Placement Predictor - Modified' in response.data
    assert b'CGPA' in response.data
    assert b'IQ' in response.data
    assert b'Profile Score' in response.data

# Test the predict route with mock input data
def test_predict(client):
    # Send a POST request with mock data to the predict route
    response = client.post('/predict', data={
        'cgpa': '3.5',
        'iq': '120',
        'profile_score': '85'
    })
    
    # Check if the response contains the expected result (i.e., 'placed' or 'not placed')
    assert b'placed' in response.data or b'not placed' in response.data
