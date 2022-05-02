import requests


def test_get_booking():
    url = 'https://restful-booker.herokuapp.com/booking/10'
    response = requests.get(url)
    assert response.status_code == 200



