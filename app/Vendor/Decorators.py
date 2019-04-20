from functools import wraps
from app.Api.Base import Base
from app.Vendor.AdminUsersAuthJWT import AdminUsersAuthJWT
from flask import request


def LoginCheck(func):
    @wraps(func)
    def WrapsLoginCheck(*args, **kwargs):
        result = AdminUsersAuthJWT().identify(request)
        if isinstance(result, str):
            return Base().error(result)
        return func(*args, **kwargs)

    return WrapsLoginCheck
