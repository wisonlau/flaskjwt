from app.Api.Base import Base
from app.Vendor.Utils import Utils
from app.Models.AdminUsers import AdminUsers
from app.env import SECRET_KEY, JWT_LEEWAY
import datetime
import jwt
import time

''' JWT工具函数在这 '''


class AdminUsersAuthJWT():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp':
                    datetime.datetime.utcnow() +
                    datetime.timedelta(seconds=JWT_LEEWAY),
                'iat':
                    datetime.datetime.utcnow(),
                'iss':
                    'wison',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, SECRET_KEY)
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    @staticmethod
    def authenticate(username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param password:
        :return: json
        """
        userInfo = AdminUsers.query.filter_by(username=username).first()
        if (userInfo is None):
            return Base().error('找不到用户')
        else:
            if (AdminUsers.check_password(userInfo.password, password)):
                login_time = int(time.time())
                AdminUsers.update(username, login_time)
                token = AdminUsersAuthJWT.encode_auth_token(userInfo.id, login_time)
                users = userInfo.to_dict()
                extend = ('id', 'password')
                for index in extend:
                    del users[index]

                return Base().successData({'token': token.decode(), 'user': users}, '登陆成功')
            else:
                return Base().error('密码不正确')

    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if (auth_header):
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT'
                    or len(auth_tokenArr) != 2):
                return '请传递正确的验证头信息'
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = AdminUsers.get(payload['data']['id'])
                    if (user is None):
                        return '找不到该用户信息'
                    else:
                        if (user.login_time == payload['data']['login_time']):
                            result = payload
                        else:
                            return 'Token已更改，请重新登录获取'
                else:
                    result = payload
        else:
            return '没有提供认证token'
        return result
