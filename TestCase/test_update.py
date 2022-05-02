import requests


def test_create_booking():

# auth token
    data_auth = {
            "username" : 'admin',
            "password" : 'password123'
        }
    auth = 'https://restful-booker.herokuapp.com/auth'
    auth_token = requests.post(auth, json=data_auth).json()['token']

    
    url_create = 'https://restful-booker.herokuapp.com/booking'

    data_create = {"firstname" : 'Bart',
        "lastname" : 'Simpson',
        "totalprice" : '111',
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : '2018-02-01',
            "checkout" : '2018-02-05'
        },
        "additionalneeds" : 'Breakfast'
        }
        
    response_create = requests.post(url_create, json=data_create).json()['bookingid']


    data_update = {"firstname" : 'Daniel',
         "lastname" : 'Mac',
        "totalprice" : '111',
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : '2018-02-01',
            "checkout" : '2018-02-05'
        },
        "additionalneeds" : 'Breakfast'
        }

    url_update = 'https://restful-booker.herokuapp.com/booking/10'


    response = requests.put(url_update, json=data_update, cookies={'token':auth_token})
    assert response.status_code == 200