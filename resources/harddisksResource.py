####################################################
#       Resources file for different resources      #
#                                                  #
####################################################

from utils import getLogger
import json
import falcon


class ProductResource(object):
    """
    Class for dealing with all products
    """
    def __init__(self):
        self.logger = getLogger()

    def on_get(self, req, resp, name):
        resp.status = falcon.HTTP_200

        self.logger.info('on_get for %s' % name)
        resp.body = json.dumps({'your name' : name})

    def on_post(self, req, resp, name):
        print(".........")