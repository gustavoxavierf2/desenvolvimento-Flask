from app import app, db
from app.models.tablesUser import User
from flask import render_template
from app.models.forms import loginForm


@app.route('/') # rota de url, atribuindo o defalt do user como nulo cado n tenha nenhum parametro previo
def index(): # pagina index
    '''usuario = User("guxfarias7", "0000", "gustavo", "guxfarias@gmail.com")
    db.session.add(usuario)
    db.session.commit()'''
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) #metodos, permitir que a pagina pegue e envie dados
def login():
    forms = loginForm() #instanciando a classe forms criada em models
    if forms.validate_on_submit(): #se o formulario for valido
        print(forms.username.data) #parametro data serve para que possamos receber os campos
        forms.username.data = None #limpando o campo de username
    else:
        print(forms.errors)
        
    return render_template('forms.html', forms=forms) #passando a instancia do forms para o html

@app.route('/teste/<user>') #passando o dados pela url
@app.route('/teste', defaults = {'user': None})
def teste(user):
    return render_template('teste.html', user = user)

@app.route('/string/<name>') #passando o dados pela url
@app.route('/string', defaults = {'name': None})
def string(name):
    if name:
        return f'teste,{name}!!'
    else:
        return 'Ola'
    
@app.route('/inteiro/<id>') #passando o dados pela url
@app.route('/inteiro')
def inteiro(id):
    id = int(id) #conversao de str para int
    print(type(id))
    return ''