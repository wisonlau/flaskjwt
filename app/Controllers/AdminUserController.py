''' 
    author: wisonlau
'''
from app import app
from app.Controllers.BaseController import BaseController
from app.Middleware.XSSProtection import XSSProtection
from app.Models.AdminUsers import AdminUsers
from app.Vendor.Utils import Utils
from flask import request
from datetime import datetime
import time
from app.Vendor.Decorators import LoginCheck


@app.route('/api/admin/register', methods=['POST'])
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
    error = BaseController().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = BaseController().getParams()
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
            return BaseController().successData(msg='添加成功')
        return BaseController().error('添加失败')
    return BaseController().error('账号已存在')


@app.route('/api/admin/adminGetList', methods=['GET'])
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
    error = BaseController().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = BaseController().getParams()
    pageNo = params['pageNo']
    pageSize = params['pageSize']
    data = AdminUsers.getList(pageNo, pageSize)
    return BaseController().json(data)


@app.route('/api/admin/adminGetOne', methods=['GET'])
@LoginCheck
def adminGetOne():
    params = BaseController().getParams()
    id = params['id']
    data = AdminUsers.query.filter_by(id=id).all()
    datas = Utils.db_l_to_d(data)
    return BaseController().successData(datas)


@app.route('/api/admin/adminEdit', methods=['POST'])
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
    error = BaseController().validateInput(rules, error_msg)
    if (error is not True):
        return error
    params = BaseController().getParams()
    if 'password' in params:
        params['password'] = AdminUsers.set_password(params['password'])
    user = AdminUsers.updateInfo(id=params['id'], data=params)

    return BaseController().successData(msg='更新成功')


@app.route('/api/admin/test', methods=['GET'])
@LoginCheck
def test():
    return 'test'
