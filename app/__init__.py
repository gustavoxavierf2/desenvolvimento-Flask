from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:FMvjqpWrp53vGZjnqqiy@containers-us-west-38.railway.app:6398/railway'
db = SQLAlchemy(app)



#from app.controllers import default

