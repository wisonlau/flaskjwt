from functools import wraps
from app.Controllers.BaseController import BaseController
from app.Vendor.AdminUsersAuthJWT import AdminUsersAuthJWT
from flask import request


def LoginCheck(func):
    @wraps(func)
    def WrapsLoginCheck(*args, **kwargs):
        result = AdminUsersAuthJWT().identify(request)
        if isinstance(result, str):
            return BaseController().error(result)
        return func(*args, **kwargs)

    return WrapsLoginCheck
