import mysql.connector

def dataBase():
    conn = mysql.connector.connect( #parametros para conexao com o banco de dados
            user='root',
            password='',
            host='',
            port='',
            database='bd(mysql)'
        )
    cursor = conn.cursor() #instancia do metodo cursor que serve para a execuçao de codigos SQL

    tabela = ()
    tabela = (''' 
        CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(20) UNIQUE KEY,
        password VARCHAR(25),
        name VARCHAR(25),
        email VARCHAR(30) UNIQUE KEY,
        teste VARCHAR(30)
        )''') #criaçao de uma tabela, que deve ser identica as classes criadas na pasta models 

    cursor.execute(tabela) #execuçao do comando sql
    _sql = 'INSERT INTO users (username, password, name, email) VALUES ("guxfarias7", "0000", "gustavo", "guxfarias@gmail.com")'
    cursor.execute(_sql)
        
    conn.commit() #upload no banco de dados
    cursor.close()
    conn.close()

dataBase()