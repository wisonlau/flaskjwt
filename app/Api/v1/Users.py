from app import app
from app.Api.Base import Base
from app.Vendor.Utils import Utils
from app.Models.Users import Users
from app.Vendor.UsersAuthJWT import UsersAuthJWT
from flask import request
from werkzeug.utils import secure_filename
import os
import base64
from flask import Blueprint

api = Blueprint('Users', __name__)
''' 注册 '''


@api.route('/Home/register', methods=['POST'])
def register():
    rules = {
        'email': {
            'required': True,
            'type': 'string',
            'minlength': 10,
            'maxlength': 20
        },
        'password': {
            'required': True,
            'type': 'string',
            'minlength': 5,
            'maxlength': 20
        }
    }
    error_msg = {
        'email': {
            'required': u'邮箱是必须的',
            'type': u'邮箱必须是字符串',
            'minlength': u'邮箱必须大于10',
            'maxlength': u'邮箱必须小于20'
        },
        'password': {
            'required': u'密码是必须的',
            'type': u'密码必须是字符串',
            'minlength': u'密码必须大于5',
            'maxlength': u'密码必须小于20'
        }
    }
    error = Base().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = Base().getParams()
    email = params['email']
    password = Users.set_password(params['password'])
    userData = Users.query.filter_by(email=email).first()
    if (userData == None):
        user = Users(
            email=email,
            password=password,
            status=1)
        user.add(user)
        if user.id:
            return Base().successData(msg='注册成功')
        return Base().error('注册失败')
    return Base().error('账号已注册')


''' 登录 '''


@api.route('/Home/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if (not email or not password):
        return Base().error('用户名和密码不能为空')
    else:
        result = UsersAuthJWT.authenticate(email, password)
        return result


'''
*获取用户信息 
*jwt中修改error处理方法,统一响应头
*_default_jwt_error_handler
'''


@api.route('/Home/user', methods=['GET'])
def get():
    # 鉴权
    result = UsersAuthJWT().identify(request)
    if isinstance(result, str):
        return Base().error(result)
    if (result['data']):
        user = Users.get(result['data']['id'])
        returnUser = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'login_time': user.login_time
        }
        return Base().successData(returnUser)
    return Base().error()


""" 不通过鉴权获取用户信息 """


@api.route('/Home/userInfo', methods=['POST'])
def getInfo():
    id = request.json.get('id')
    data = Users.query.filter_by(id=id).all()
    datas = Utils.db_l_to_d(data)
    return Base().successData(datas)
