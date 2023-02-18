from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # atribuiçao do Flask
app.config.from_object('config') # setando as configs
db = SQLAlchemy(app) # atribuiçao do banco de dados a variavel db

#import de tabelas diretamente utilizaveis na aplicaçao, para que o arquivo run.py possa reconhecer
from app.models import tablesUser
from app.controllers import default

