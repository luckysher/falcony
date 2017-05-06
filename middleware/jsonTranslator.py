########################################################
##     Json translator for the falcony rest api       ##
##                                                    ##
########################################################

import falcon
import json

from error import InvalidError


class JSONTranslator(object):

    def process_request(self, req, res):
        req.context['data'] = None
        #  check if any data is provided
        if req.content_length is None:
            return
        if req.content_type == 'application/json' or req.content_type == 'text/plain':
            try:
                raw_json = req.stream.read()
            except Exception as e:
                raise falcon('bad request', e)
            try:
                req.context['data'] = raw_json
            except ValueError:
                raise InvalidError('json decoding error or malformed json ')

        if req.get_header('Authorization'):
            req.context['auth_user'] = req.get_header('Authorization')

    def process_response(self, req, resp, resource):
        if 'data' not in req.context:
            return


