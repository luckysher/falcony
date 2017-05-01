
from error import UnAuthorizedUser


def auth_required(req, res, resource):
    if req.context['auth_user'] is None:
        raise UnAuthorizedUser()