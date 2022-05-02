import requests


def test_create_booking():

    url = 'https://restful-booker.herokuapp.com/booking'

    data = {"firstname" : 'Bart',
        "lastname" : 'Simpson',
        "totalprice" : '111',
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : '2018-02-01',
            "checkout" : '2018-02-05'
        },
        "additionalneeds" : 'Breakfast'
        }
        

    response = requests.post(url, json=data)
    assert response.status_code == 200
    