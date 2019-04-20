''' 
    author: wisonlau
'''
from app import app
from app.Api.Base import Base
from app.Middleware.XSSProtection import XSSProtection
from app.Models.AdminUsers import AdminUsers
from app.Vendor.AdminUsersAuthJWT import AdminUsersAuthJWT
from app.Vendor.Utils import Utils
from flask import request
from flask import Blueprint

api = Blueprint('Login', __name__)
''' 登录 '''


@api.route('/admin/login', methods=['POST'])
def adminLogin():
    rules = {
        'username': {
            'required': True,
        },
        'password': {
            'required': True,
        }
    }
    error_msg = {
        'username': {
            'required': u'用户名是必须的',
        },
        'password': {
            'required': u'密码是必须的',
        }
    }
    error = Base().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = Base().getParams()
    username = params['username']
    password = params['password']
    if (not username or not password):
        return Base().error('用户名和密码不能为空')
    else:
        result = AdminUsersAuthJWT.authenticate(username, password)
        return result


'''
*获取用户信息 
*jwt中修改error处理方法,统一响应头
*_default_jwt_error_handler
'''


@api.route('/admin/user', methods=['GET'])
def getJWT():
    # 鉴权
    result = AdminUsersAuthJWT().identify(request)
    if isinstance(result, str):
        return Base().error(result)
    if (result['data']):
        user = AdminUsers.get(result['data']['id'])
        returnUser = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'login_time': user.login_time
        }
        return Base().successData(returnUser)
    return Base().error()


@api.route('/admin/LoginTest', methods=['GET'])
def test():
    return 'LoginTest'
