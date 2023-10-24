from marshmallow import fields
from app.ext import ma

class CandidatoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    edad = fields.Integer()
    numero = fields.Integer()


class PartidoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    candidatoP = fields.Nested('CandidatoSchema', many=False)

class VotoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    candidato = fields.Nested('CandidatoSchema', many=False)
    partido = fields.Nested('PartidoSchema', many=False)
