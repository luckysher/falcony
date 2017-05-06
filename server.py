##################################################
##                                              ##
##        Main file for running the server      ##
##################################################

import falcon
from wsgiref import simple_server
from utils import getLogger

from middleware.jsonTranslator import JSONTranslator
# import products
from resources.productResource import ProductsResource
from resources.baseResource import BaseResource
from resources.usersResource import UsersResource
from resources.baseResource import handle_404


logger = getLogger()

# falcon app with middleware
app = falcon.API(middleware=[JSONTranslator()])
login = UsersResource()
home = BaseResource()
products = ProductsResource()

# add app routes
# route for all products
app.add_route('/home', home)
app.add_route('/login', login)
app.add_route('/products', products)

# handler for not found resources
app.add_sink(handle_404, '')

# add error handlers


# main for server
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    logger.debug("Starting  server on http://%s:%d/" % (host, port))
    server = simple_server.make_server(host, port, app)
    server.serve_forever()