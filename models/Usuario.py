from utils import db

class Usuario(db.Model):
    __tablename__='usuario'
    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement=True) 
    nome = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(200))
    senha = db.Column(db.String(200))
<<<<<<< HEAD
    user_tipo = db.Column(db.Integer)
=======
    tipo_user = db.Column(db.Integer)
>>>>>>> d35a044080fde2211f0cf59fe58e145414fc7489


    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)