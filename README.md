# falcony
Restfull api for computer products written in falcon

![basic-feature](https://github.com/luckysher/falcony/blob/master/mockup.png)

Post Json request example
=========================
curl -XPOST http://127.0.0.1:8000/login -H 'Content-Type:application/json' -d '{"username" : "john123", "password": "12345678" }'

    response:
    {
        "meta": {
                "code": "200",
                "status": "Ok"
            },

        "data": {
                "username": "john123",
                 "token": "N2MyMjJmYjI5MjdkODI4YWYyMmY1OTIxMzRlODkzMjQ4MDYzN2MwZA=="
             }
    }


Get request example
=========================
curl -XGET http://127.0.0.1:8000/products

    {
        "meta": {
                "code": "200",
                "status": "Ok"
                },
        "data": {
                "Harddisks": {
                                "quantity": 15,
                                "name": "Harddisks",
                                "manufacturers": ["WD", "SEAGATE"]
                             },
                "Headphone": {
                                "quantity": 5,
                                "name": "Headphone",
                                 "manufacturers": ["Intex"]
                              }
                }
    }


Handle not found requests example
===================================
    curl -XGET http://127.0.0.1:8000/processors

    {
        "available_urls": {
                            "1.": "/login",
                            "2.": "/products",
                            "3.": "/orders",
                            "4.": "/harddisks",
                            "5.": "/headphones"
                          },
                            "code": 404,
                            "error": "not found: Path=/processors"
                          }
    }
