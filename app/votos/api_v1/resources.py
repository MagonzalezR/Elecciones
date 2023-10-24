from flask import request, Blueprint
from flask_restful import Api, Resource
from .schemas import CandidatoSchema, PartidoSchema, VotoSchema
from ..models import Candidato, Partido, Voto

elecciones_v1_bp = Blueprint('elecciones_v1_bp', __name__)
candidato_schema = CandidatoSchema()
partido_schema = PartidoSchema()
voto_schema = VotoSchema()

api = Api(elecciones_v1_bp)
class CandidatoResource(Resource):
    def get(self, candidato_id):
        candidato = Candidato.get_by_id(candidato_id)
        resp = candidato_schema.dump(candidato)
        return resp
    
    def post(self):
        data = request.get_json()
        cand_dict = candidato_schema.load(data)
        candidato = Candidato(nombre=cand_dict['nombre'],
                    edad=cand_dict['edad'],
                    numero=cand_dict['numero'],
        )
        candidato.save()
        resp = candidato_schema.dump(candidato)
        return resp, 201
    
api.add_resource(CandidatoResource, '/api/v1/candidato/<int:candidato_id>', endpoint='candidato_resource')

class PartidoResource(Resource):
    def get(self, partido_id):
        partido = Partido.get_by_id(partido_id)
        resp = partido_schema.dump(partido)
        return resp

    def post(self):
        data = request.get_json()
        par_dict = partido_schema.load(data)
        partido = Candidato(nombre=par_dict['nombre'],
                    candidatoP= par_dict['candidatoP'])
        partido.save()
        resp = partido_schema.dump(partido)
        return resp, 201

api.add_resource(PartidoResource, '/api/v1/candidato/<int:candidato_id>', endpoint='partido_resource')

class VotoResource(Resource):
    def get(self, voto_id):
        voto = Partido.get_by_id(voto_id)
        resp = voto_schema.dump(voto)
        return resp
    
    def post(self):
        data = request.get_json()
        voto_dict = voto_schema.load(data)
        voto = Candidato(partido=voto_dict['partido'],
                    candidato= voto_dict['candidato'])
        voto.save()
        resp = voto_schema.dump(voto)
        return resp, 201
    
api.add_resource(VotoResource, '/api/v1/candidato/<int:candidato_id>', endpoint='voto_resource')