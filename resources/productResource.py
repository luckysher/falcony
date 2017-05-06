from models import Harddisks, Headphone
from baseResource import BaseResource
import json
import falcon
from hooks import auth_required
from dbUtils import ( getSession,
                      getEngine,
                      db_url,
                      getProductDetails)


class ProductsResource(BaseResource):
    """
    class for all products resource
    """

    # handler for all products request
    def on_get(self, req, res):
        # set response status 'ok'
        res.status = falcon.HTTP_200
        # get all products list
        productsList = []
        session = getSession(getEngine(db_url))
        # get all harddisks
        harddisks = session.query(Harddisks).all()
        if harddisks:
            productsList.append(harddisks)

        #get all headphones
        headphones = session.query(Headphone).all()

        if headphones:
            productsList.append(headphones)

        product_details_dict = json.dumps(getProductDetails(productsList))
        self.on_success(res, product_details_dict)

