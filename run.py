from app import app #instancia do Flask, contida na variavel app da pasta app
from prepare_db import dataBase

if __name__ == "__main__":
    #dataBase()
    app.run() #executa a aplicaçao