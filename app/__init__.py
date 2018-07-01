# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # 蓝本在工厂函数create_app()中注册到程序上
    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from .manager import manager as manager_blueprint
    app.register_blueprint(manager_blueprint)

    # 附加路由和自定义的错误页面

    return app  # 工厂函数返回创建的程序示例

