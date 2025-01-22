from utils import db

class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement=True) 
    nome = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(200))
    senha = db.Column(db.String(200))
    tipo_user = db.Column(db.Integer)


    def __init__(self, nome, telefone, email, senha, tipo_user):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.tipo_user = tipo_user

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)