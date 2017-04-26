##################################################
##                                              ##
##        Main file for running the server      ##
##################################################

import falcon
from wsgiref import simple_server
from utils import getLogger

# import products
from resources.productsResource import ProductResource

logger = getLogger()

# falcon app with middleware
app = falcon.API()

products = ProductResource()

# add app routes
# route for all products
app.add_route('/{name}/products', products)

# add error handlers


# main for server
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    logger.debug("Starting  server on http://%s:%d/" % (host, port))
    server = simple_server.make_server(host, port, app)
    server.serve_forever()