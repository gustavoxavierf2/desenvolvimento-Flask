from app import db #instancia do banco de dados

class User(db.Model): #classe user extendendo db.Model, PADRAO para todas a classes de tabela
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