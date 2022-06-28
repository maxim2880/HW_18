from flask import request, make_response
from flask_restx import api, Resource, namespace, Api, Namespace

from dao.model.directors import DirectorSchema
from implemented import director_service
directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)
    def get(self):
        return self.schema.dump(director_service.get()), 200


@directors_ns.route('/<int:did>')
class GenreView(Resource):
    schema = DirectorSchema()
    def get(self, did):
        return self.schema.dump(director_service.get(did)), 200

