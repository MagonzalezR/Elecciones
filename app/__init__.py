from flask import Flask, jsonify
from flask_restful import Api
from app.db import db
from app.votos.api_v1.resources import elecciones_v1_bp
from .ext import ma, migrate

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    # Captura todos los errores 404
    Api(app, catch_all_404s=True)
    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False
    # Registra los blueprints
    app.register_blueprint(elecciones_v1_bp)
    # Registra manejadores de errores personalizados
    return app