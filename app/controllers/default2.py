from app import app

@app.route('/teste2') # rota de url, atribuindo o defalt do user como nulo cado n tenha nenhum parametro previo
def teste2(): # pagina index
    return" OK"