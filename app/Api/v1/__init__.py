def create_blueprint_v1(app):
    dicts = {'AdminUser': 'AdminUserApi', 'Login': 'LoginApi', 'Users': 'UsersApi'}
    for index in dicts:
        exec (f'from app.Api.v1.{index} import api as {dicts[index]}')
        exec (f'app.register_blueprint({dicts[index]}, url_prefix="/v1")')
