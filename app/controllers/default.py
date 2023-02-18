from app import app, db
from app.models.tablesUser import user

@app.route('/') # rota de url
def index(): # pagina index
    k = user("tggggggggt", "sadgfas", "sdfdsaf", "fsdg@gmail")
    db.session.add(k)
    db.session.commit()
    return 'tezzte, testando'