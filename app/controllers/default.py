from app import app, db
from app.models.tablesUser import User
from flask import render_template

@app.route('/<user>')
@app.route('/',  defaults = {'user': None}) # rota de url
def index(user): # pagina index
    '''usuario = User("guxfarias7", "0000", "gustavo", "guxfarias@gmail.com")
    db.session.add(usuario)
    db.session.commit()'''
    return render_template('teste.html', user = user)

@app.route('/teste/<name>')
@app.route('/teste', defaults = {'name': None})
def teste(name):
    if name:
        return f'teste,{name}!!'
    else:
        return 'Ola'
    
@app.route('/inteiro/<id>')
@app.route('/inteiro')
def inteiro(id):
    id = int(id) #conversao de str para int
    print(type(id))
    return ''