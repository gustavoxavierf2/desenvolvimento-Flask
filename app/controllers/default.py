from app import app, db
from app.models.tablesUser import User
from flask import render_template, flash
from app.models.forms import loginForm
from flask_login import login_user, logout_user


@app.route('/') # rota de url, atribuindo o defalt do user como nulo cado n tenha nenhum parametro previo
def index(): # pagina index
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) #metodos, permitir que a pagina pegue e envie dados
def login():
    forms = loginForm() #instanciando a classe forms criada em models
    if forms.validate_on_submit(): #se o formulario for valido
        print(forms.username.data) #parametro data serve para que possamos receber os campos
        #forms.username.data = None #limpando o campo de username
        
        user = User.query.filter_by(username=forms.username.data).first()#filtro pegando o primeiro user do bd que corresponda ao username q foi digitado no formulario
        if user and user.password == forms.password.data:#se user existir e a senha do bd for igual a senha passada no forms
            login_user(user)#loga o usuario
            print('logado')
            flash('logado')
        else:
            print('login invalido')
            flash('login invalido')
    else:
        print(forms.errors)
        
    return render_template('forms.html', forms=forms) #passando a instancia do forms para o html

@app.route('/logout')
def logout():
    logout_user()#desloga o usuario
    print('sai')
    return app.redirect(app.url_for('login'))

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
@app.route('/inteiro', defaults = {'id': 0})
def inteiro(id):
    id = int(id) #conversao de str para int
    print(type(id))
    return f'{id}, o tipo e retornado no terminal'

@app.route('/crud')
def crud():
    try:
        create = User("gustavo", "0000", "gustav", "gguggu@gmail.com")#username e email sao unique
        db.session.add(create)#adicionando na sessao
        db.session.commit()#salvando as alteraçoes no banco de dados
    except:
        print('error')
    
    select = User.query.filter_by(password='0000').first()#all() #filtro pegando o primeiro user que corresponda a senha tal'{0000}'
    print(select.name)
    
    select.name = 'gugu' #update, substituindo o name do banco de dados
    db.session.add(select)#adicionando na sessao
    db.session.commit()#salvando as alteraçoes no banco de dados
    print(select.name)
    
    '''db.session.delete(select)#adicionando na sessao
    print('deletando', select.name)
    db.session.commit()#salvando as alteraçoes no banco de dados'''
  
    return 'select ok'