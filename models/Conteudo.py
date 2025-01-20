from Splan.utils import db

class Conteudo(db.Model):
    __tablename__='conteudo'
    id_conteudo = db.column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.column(db.String(150))
    id_assunto = db.column(db.Integer, db.ForeigKey('assunto.id_assunto'))


    def __init__(self, nome, id_assunto):
        self.nome = nome
        self.id_assunto = id_assunto

    def __repr__(self):
        return "<Conteudo {}>".format(self.nome)
