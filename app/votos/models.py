from app.db import db, BaseModelMixin


class Candidato(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True) #identificador 
    nombre = db.Column(db.String)                #nombre candidato
    edad = db.Column(db.Integer)                 #edad del candidato
    numero = db.Column(db.Integer)               #numero tarjeton
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)


    def __init__(self, nombre, edad, numero):
        self.nombre = nombre
        self.edad = edad
        self.numero = numero

    def __repr__(self):
        return f'Candidato ({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'


class Partido(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    candidatoP = db.relationship('Candidato', backref='candidato', lazy=False, cascade='all, delete-orphan')
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Partido ({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'
    
class Voto(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    candidato = db.relationship('Candidato', backref='candidato', lazy=False, cascade='all, delete-orphan')
    partido = db.relationship('Partido', backref='partido', lazy=False, cascade='all, delete-orphan')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'voto ({self.id})'

    def __str__(self):
        return f'{self.id}'