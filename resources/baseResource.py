#########################################################
#           Base class for all resources                #
#########################################################

import json
from collections import OrderedDict
import falcon

from error import NotSupportedError


falcony_home = {
        'appname': 'Falcony',
        'message': 'Welcome to falcony rest-api'
}

# base and home for the falcony rest-api
class BaseResource(object):
    """
    base class for all resources
    """
    def to_json(self, data):
        return json.dumps(data)

    def set_cors_headers(self, res):
        res.set_header('Access-Control-Allow-Origin', '*');

    def on_success(self, res, data):
        res.status = falcon.HTTP_200
        self.set_cors_headers(res)
        meta = OrderedDict()
        meta['code'] = '200'
        meta['status'] = 'Ok'

        resObj = OrderedDict()
        resObj['meta'] = meta
        resObj['data'] = json.loads(data)

        res.body = self.to_json(resObj)
        print json.dumps(meta)

    def on_error(self, res, error):
        res.status = error['status']
        self.set_cors_headers(res)
        meta = OrderedDict()
        meta['status'] = error['status']
        meta['code'] = error['code']
        meta['message'] = error['title']

        resObj = OrderedDict()
        resObj['meta'] = meta
        res.body = self.to_json(resObj)

    def on_get(self, req, res):
        if req.path == '/':
            res.status = falcon.HTTP_200
            res.body = self.to_json(falcony_home)
        else:
            raise NotSupportedError(method='GET', url=req.path)

    def on_post(self, req, res):
        raise NotSupportedError(method='POST', url=req.path)

    def on_put(self, req, res):
        raise NotSupportedError(method='PUT', url=req.path)

    def on_delete(self, req, res):
        raise NotSupportedError(method='DELETE', url=req.path)


def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    avail_urls = OrderedDict()
    avail_urls['1.'] = '/login'
    avail_urls['2.'] = '/products'
    avail_urls['3.'] = 'harddisks'

    message = {
        'error': 'not found: Path=' + req.path,
        'code': 404,
        'available_urls': avail_urls
    }
    resp.body = json.dumps(message)