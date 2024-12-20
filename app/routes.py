from flask_restful import Resource, Api
from flask import render_template, make_response, request
from flask_jwt_extended import jwt_required
from .methods import user_register, user_login

class Registro(Resource):
    def post(self):
        user_info = request.get_json()
        respuesta, status = user_register(
            user_info.get('nombre'),
            user_info.get('correo'),
            user_info.get('telefono'),
            user_info.get('password')
        )
        return respuesta, status

class Login(Resource):
    def post(self):
        user_info = request.get_json()
        respuesta, status = user_login(
            user_info.get('correo'),
            user_info.get('password')
        )
        return respuesta, status

class Restringido(Resource):
    @jwt_required()
    def get(self):
        return {'mensaje': 'Acceso autorizado'}, 200

def init_api(app):
    api = Api(app)
    api.add_resource(Registro, '/registro')
    api.add_resource(Login, '/login')
    api.add_resource(Restringido, '/restringido')






