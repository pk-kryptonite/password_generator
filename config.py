import uuid

class Config:
    SECRET_KEY = str(uuid.uuid4().hex)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/password_generator'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
