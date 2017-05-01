from error import UNAUTHORIZED_USER

# middle ware for authenticating user
class AuthMiddleware(object):

    def process_request(self, req, resp):
        token = req.get_header('Authorization')
        user_id = req.get_header('user_id')
        if token is None:
            description = "Authentication token not provided.Please provide authentication token"
            raise UNAUTHORIZED_USER(description=description)
        if not self.is_token_valid(token):
            description = "Authentication required.Please get new token and try again.."
            raise UNAUTHORIZED_USER(description=description)

    def is_token_valid(self, token):
        pass