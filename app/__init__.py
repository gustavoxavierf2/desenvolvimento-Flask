from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__) # atribuiçao do Flask
app.config.from_object('config') # setando as configs ##pyfile
db = SQLAlchemy(app) # atribuiçao do banco de dados a variavel db
lm = LoginManager() # atribuiçao do loginManeger a variavel lm
lm.init_app(app) #iniciaçao do loginManeger

#import de tabelas diretamente utilizaveis na aplicaçao, para que o arquivo run.py possa reconhecer
from app.models import tablesUser, forms
from app.controllers import default, default2

