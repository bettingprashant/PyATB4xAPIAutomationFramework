def payload_create_booking():

    payload = {
        "firstname": "Prashant",
        "lastname": "Raj",
        "totalprice": "Raj",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "breakfast"
    }
    return payload

def payload_create_token():
    payload = {
        "username" : "admin",
        "password" : "password123"
    }
    return payload