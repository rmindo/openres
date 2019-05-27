#!/usr/bin/env python


from flask_cors import CORS
# HTTP
from src.routes.http import HTTP
# API Versions
from src.services.invoices.apione import apione


api = {}

# HTTP
http = HTTP()

# Cross Origin
CORS(http.flask)


# API Versions
api['v1'] = apione(http)



# API Routes
http.api(http, api)




# Handle not found error
@http.flask.errorhandler(404)
# Not Found
def notfound(e):

    return http.response([], 404)




# Handle method not allowed error
@http.flask.errorhandler(405)
# Not Allowed
def notallowed(e):

    return http.response([], 405)




# Run the App
if __name__ == '__main__':

    http.flask.run(debug=True, port=200)