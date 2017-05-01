import falcon
from collections import OrderedDict
import json


ERR_UNKNOWN = {
    'status': falcon.HTTP_500,
    'code': 500,
    'title': 'Unknown Error'
}

UNAUTHORIZED_USER = {
    'status': falcon.HTTP_401,
    'code': 99,
    'title': 'User not authorized'
}

NOT_SUPPORTED_ERROR = {
    'status': falcon.HTTP_404,
    'code': 10,
    'title': 'Not supported'
}

INVALID_ERROR = {
    'status': falcon.HTTP_400,
    'code': 88,
    'title': 'Invalid Parameter'
}

# base class for all falcony errors
class Error(Exception):

    def __init__(self, error=ERR_UNKNOWN, description=None):
        self.error = error
        self.error['description'] = description

    @property
    def code(self):
        return self.error['code']

    @property
    def title(self):
        return self.error['title']

    @property
    def status(self):
        return self.error['status']

    @property
    def description(self):
        return self.error['description']

    @staticmethod
    def handle(ex, req, resp, error):
        resp.status = ex.status

        meta = OrderedDict()
        meta['code'] = ex.code
        meta['message'] = ex.title

        if error['description']:
            meta['description'] = error['description']
        resp.body = json.dumps({'meta': meta})


# class for handling unauthorized user
class UnAuthorizedUser(Error):
    def __init__(self, description=None):
        super.__init__(UNAUTHORIZED_USER)
        if description:
            self.error['description'] = description


class NotSupportedError(Error):
    def __init__(self, method=None, url=None):
        super.__init__(NOT_SUPPORTED_ERROR)
        if method and url:
            self.error['description'] = 'Method: %s, Url: %s' % (method, url)


class InvalidError(Error):
    def __init__(self, description=None):
        super.__init__(INVALID_ERROR)
        if description:
            self.error['description'] = description