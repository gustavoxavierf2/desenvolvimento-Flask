from app import db, lm #instancia do banco de dados e LoginManager
from flask_login import UserMixin #LoginManager 

#login verification in database
@lm.user_loader
def get_user(user_id):
    User.query.filter_by(id=user_id).first()
class User(db.Model, UserMixin): #classe user extendendo db.Model, PADRAO para todas a classes de tabela
# classe user extendendo UserMixin, para podermos consultar no bd o login do user

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    #PADRAO
    def __init__(self,username,password, name, email):
       self.username = username
       self.password = password
       self.name = name
       self.email = email
       
    def __repr__(self):
        return '<user %r>' % self.username