# mysql
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_DB = 'auth'
DB_CHARSET = 'utf8'
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_DB + '?charset=' + DB_CHARSET
SQLALCHEMY_TRACK_MODIFICATIONS = True
# debug
DEBUG_LOG = True
# upload
UPLOAD_FOLDER = '/uploads/'  # 允许目录
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 允许大小16MB
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])  # 允许文件
# jwt
SECRET_KEY = '7PXsHcHGfa4e3kEs8Rvcv8ymjI0UeauX'
JWT_LEEWAY = 604800
