from Splan.utils import db

class Progresso(db.Model):
    __tablename__='progresso'
    id_progresso = db.column(db.Integer, primary_key = True, autoincrement = True)
    concluido = db.column(db.Integer)
    tempo_estudado = db.column(db.Float)
    id_usuario = db.column(db.Integer, db.ForeigKey('usuario.id_usuario'))
    id_assunto = db.column(db.Integer, db.ForeigKey('assunto.id_assunto'))
    

    def __init__(self, concluido, tempo_estudado, id_usuario, id_assunto):
        self.concluido = concluido
        self.tempo_estudado = tempo_estudado
        self.id_usuario = id_usuario
        self.id_assunto = id_assunto

    def __repr__(self):
        return "<Progresso {}>".format(self.concluido)
