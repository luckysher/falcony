##.........................................##
##    Utility functions                    ##
##.........................................##

import logging
import base64
import hashlib
from settings import APP_NAME


# function for getting logger
def getLogger():
    logging.basicConfig(format='%(name):%(levelname)s: %(message)s')
    logger = logging.getLogger(APP_NAME)
    return logger


# function for getting token from the string
def strToToken(password):
    utfEncStr = password.encode('utf-8')
    token = None
    try:
        sha_1 = hashlib.sha1()
        sha_1.update(utfEncStr)
        token = base64.b64encode(sha_1.hexdigest())
    except Exception as e:
        print("Got exception while generating token: %s" % e)

    return token
