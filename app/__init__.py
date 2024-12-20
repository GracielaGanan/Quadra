#init.Py

from flask import Flask, jsonify
from flask_restful import Api
from .routes import APIRoutes
from .config import Config
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from .extensions import db, jwt

def configurar_app():
    # Inicializa la aplicación Flask
    app = Flask(__name__)

    # Configura la app con los valores de Config
    app.config.from_object(Config)

    # Inicializa la base de datos y JWT
    db.init_app(app)
    jwt.init_app(app)

    # Crea todas las tablas en la base de datos
    with app.app_context():
        db.create_all()

    # Configura las rutas de la API
    api = Api(app)
    rutas = APIRoutes()
    rutas.init_api(api)

    # Manejo de errores personalizados
    @app.errorhandler(NoAuthorizationError)
    def handle_no_token(e):
        return jsonify({"message": "Se requiere un token de autorización.", "error": str(e)}), 401

    @app.errorhandler(InvalidHeaderError)
    def handle_invalid_token(e):
        return jsonify({"message": "Token inválido o mal formado.", "error": str(e)}), 422

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "El token ha expirado.", "error": "token_expired"}), 401

    # Devuelve la aplicación configurada
    return app







