from app import db
from app.Models.BaseModel import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils
from datetime import datetime


class AdminUsers(db.Model, BaseModel, SerializerMixin):
    __tablename__ = 'admin_users'
    __schema_extend__ = ('-password',)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(190))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    avatar = db.Column(db.String(255), nullable=True)
    remember_token = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    login_time = db.Column(db.Integer, nullable=True)

    # 设置密码
    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    # 校验密码
    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)

    # 获取用户信息
    @staticmethod
    def get(id):
        return AdminUsers.query.filter_by(id=id).first()

    # 获取用户信息列表
    @staticmethod
    def getList(page, per_page):
        page = int(page)
        per_page = int(per_page)
        dataObj = AdminUsers.query.order_by(AdminUsers.created_at.desc()).paginate(page, per_page=per_page,
                                                                                   error_out=False)
        paginate = BaseModel.formatPaged(page, per_page, dataObj.total)
        list = Utils.db_l_to_d(dataObj.items)
        data = BaseModel.formatBody(
            {"paged": paginate, "list": list})
        return data

    # 增加用户
    def add(self, user):
        db.session.add(user)
        return db.session.commit()

    # 根据id删除用户
    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return db.session.commit()

    # 更新登录时间
    @staticmethod
    def update(username, login_time):
        AdminUsers.query.filter_by(username=username).update({'login_time': login_time})
        return db.session.commit()

    # 更新用户信息
    @staticmethod
    def updateInfo(id, data):
        AdminUsers.query.filter_by(id=id).update(data)
        return db.session.commit()
