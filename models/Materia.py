from utils import db

class Materia(db.Model):
    __tablename__='materia'
    id_materia = db.column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.column(db.String(150))


    def __init__(self, nome):
        self.nome = nome 

    def __repr__(self):
        return "<Materia {}>".format(self.nome)