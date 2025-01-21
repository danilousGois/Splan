from utils import db

class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement=True) 
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(250))


    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)