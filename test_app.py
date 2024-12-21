import pytest
from app import app
import pickle
import numpy as np

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

test_data = {
    'cgpa': 8.0,
    'iq': 120,
    'profile_score': 85
}

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'placement predictor' in response.data  

# Test for the predict placement route
def test_predict_placement(client):
    # Simulate a POST request to the '/predict' route with test data
    response = client.post('/predict', data=test_data)

    # Ensure the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the result ('placed' or 'not placed') is in the response
    assert b'placed' in response.data or b'not placed' in response.data

# Test model prediction functionality (without the Flask app)
def test_model_prediction():
    # Load the model
    model = pickle.load(open('model.pkl', 'rb'))

    # Input data for prediction
    input_data = np.array([8.0, 120, 85]).reshape(1, 3)

    # Make a prediction
    result = model.predict(input_data)

    # Assert that the result is either 0 or 1 (for 'not placed' or 'placed')
    assert result[0] in [0, 1]
