##.........................................##
##    Utility functions                    ##
##.........................................##

import logging
APP_NAME = 'Falcony'

# function for getting logger
def getLogger():
    logging.basicConfig(format='%(name):%(levelname)s: %(message)s')
    logger = logging.getLogger(APP_NAME)
    return logger

