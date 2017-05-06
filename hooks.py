
from error import UnAuthorizedUser


def auth_required(req, res, resource, param):
    if req.get_header('Authorization') is None:
        raise UnAuthorizedUser()