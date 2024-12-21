from flask_restful import Api, Resource
from flask import render_template, make_response, request
from flask_jwt_extended import jwt_required
from .methods import user_register, user_login
from flask import Blueprint

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

   
# Simplemente se va a encargar de darle rutas a mis recursos
class APIRoutes:
    def init_api(self, api):
    api.add_resource(HolaMundo, '/')
    api.add_resource(Registro, '/registro')
    api.add_resource(Login, '/login')
    api.add_resource(Restringido, '/restringido')

    APIRoutes = Blueprint('api', __name__)
    api = Api(APIRoutes)

    @APIRoutes.route('/status', methods=['GET'])
    def status():
        return {'status': 'Running'}







