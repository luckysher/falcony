#######################################################
##      Added resources file for users               ##
##      related functionalities like login, logout   ##
#######################################################

from resources.baseResource import BaseResource
import json
from collections import OrderedDict
from error import UNAUTHORIZED_USER
from dbUtils import ( isUserAuthenticated,
                      getSession,
                      getEngine,
                      db_url)

class UsersResource(BaseResource):
    """
    class handling users login and logout requests
    """

    def on_post(self, req, res):
        data = OrderedDict()
        userdata = json.loads(req.context['data'])
        # get user name and password for login
        username = userdata['username']
        password = userdata['password']

        session = getSession(getEngine(db_url))
        token = isUserAuthenticated(session, username, password)
        if token:
            data['username'] = username
            data['token'] = token
            self.on_success(res, json.dumps(data))
        else:
            data['username'] = username
            data['token'] = token
            self.on_error(res, UNAUTHORIZED_USER)




