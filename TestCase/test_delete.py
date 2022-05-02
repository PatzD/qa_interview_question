import requests


def test_get_booking():

# creating auth token
    data_auth = {
            "username" : 'admin',
            "password" : 'password123'
        }

    auth = 'https://restful-booker.herokuapp.com/auth'
    response_auth = requests.post(auth, json=data_auth).json()['token']


    url = 'https://restful-booker.herokuapp.com/booking/8'
    response = requests.delete(url, cookies={'token':response_auth})
    assert response.status_code == 201



