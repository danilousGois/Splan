from utils import db

class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.column(db.String(150))
    telefone = db.column(db.String(20))
    email = db.column(db.String(100))
    senha = db.column(db.String(250))


    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)