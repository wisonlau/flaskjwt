''' 
    author: wisonlau
'''
from app import app
from app.Api.Base import Base
from app.Middleware.XSSProtection import XSSProtection
from app.Models.AdminUsers import AdminUsers
from app.Vendor.Utils import Utils
from flask import request
from datetime import datetime
import time
from app.Vendor.Decorators import LoginCheck
from flask import Blueprint

api = Blueprint('AdminUser', __name__)


@api.route('/admin/register', methods=['POST'])
@LoginCheck
def adminAdd():
    rules = {
        'username': {
            'required': True,
            'type': 'string',
            'minlength': 4,
            'maxlength': 20
        },
        'password': {
            'required': True,
            'type': 'string',
            'minlength': 5,
            'maxlength': 20
        },
        'name': {
            'required': False,
            'type': 'string',
            'minlength': 5,
            'maxlength': 20
        }
    }
    error_msg = {
        'username': {
            'required': u'用户名是必须的',
            'type': u'用户名必须是字符串',
            'minlength': u'用户名必须大于4',
            'maxlength': u'用户名必须小于20'
        },
        'password': {
            'required': u'密码是必须的',
            'type': u'密码必须是字符串',
            'minlength': u'密码必须大于5',
            'maxlength': u'密码必须小于20'
        },
        'name': {
            'type': u'昵称必须是字符串',
            'minlength': u'昵称必须大于5',
            'maxlength': u'昵称必须小于20'
        }
    }
    error = Base().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = Base().getParams()
    username = params['username']
    password = AdminUsers.set_password(params['password'])
    name = params['name']
    login_time = int(time.time())
    userData = AdminUsers.query.filter_by(username=username).first()
    if (userData == None):
        user = AdminUsers(
            username=username,
            password=password,
            name=name,
            login_time=login_time,
        )
        user.add(user)
        if user.id:
            return Base().successData(msg='添加成功')
        return Base().error('添加失败')
    return Base().error('账号已存在')


@api.route('/admin/adminGetList', methods=['GET'])
@LoginCheck
def adminGetList():
    rules = {
        'pageNo': {
            'required': True,
        },
        'pageSize': {
            'required': True,
        }
    }
    error_msg = {
        'pageNo': {
            'required': u'当前页是必须的',
        },
        'pageSize': {
            'required': u'当前页是必须的',
        }
    }
    error = Base().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = Base().getParams()
    pageNo = params['pageNo']
    pageSize = params['pageSize']
    data = AdminUsers.getList(pageNo, pageSize)
    return Base().json(data)


@api.route('/admin/adminGetOne', methods=['GET'])
@LoginCheck
def adminGetOne():
    params = Base().getParams()
    id = params['id']
    data = AdminUsers.query.filter_by(id=id).all()
    datas = Utils.db_l_to_d(data)
    return Base().successData(datas)


@api.route('/admin/adminEdit', methods=['POST'])
@LoginCheck
def adminEdit():
    rules = {
        'id': {
            'required': True,
        },
        'username': {
            'type': 'string',
            'minlength': 4,
            'maxlength': 20
        },
        'password': {
            'type': 'string',
            'minlength': 5,
            'maxlength': 20
        },
        'name': {
            'type': 'string',
            'minlength': 5,
            'maxlength': 20
        }
    }
    error_msg = {
        'username': {
            'required': u'ID是必须的',
        },
        'username': {
            'type': u'用户名必须是字符串',
            'minlength': u'用户名必须大于4',
            'maxlength': u'用户名必须小于20'
        },
        'password': {
            'type': u'密码必须是字符串',
            'minlength': u'密码必须大于5',
            'maxlength': u'密码必须小于20'
        },
        'name': {
            'type': u'昵称必须是字符串',
            'minlength': u'昵称必须大于5',
            'maxlength': u'昵称必须小于20'
        }
    }
    error = Base().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = Base().getParams()
    if 'password' in params:
        params['password'] = AdminUsers.set_password(params['password'])
    user = AdminUsers.updateInfo(id=params['id'], data=params)

    return Base().successData(msg='更新成功')


@api.route('/admin/AdminUserTest', methods=['GET'])
@LoginCheck
def test():
    return 'AdminUser'
