from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class loginForm(FlaskForm): # criando modelo/classe utilizavel pelo flask
    username = StringField('username', validators=[DataRequired()]) #validadores DataRequired(), indicam q este campo deve estar preenchido
    #name = StringField('name', validators=[DataRequired()]) #validadores DataRequired(), indicam q este campo deve estar preenchido
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember')