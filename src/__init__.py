from flask import Flask

from .controlador import rutasCuenta, rutasUsuario, rutasInicio, rutasMovimiento

app = Flask(__name__,template_folder="./vista")

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(rutasInicio.main, url_prefix='/Home')
    app.register_blueprint(rutasUsuario.main, url_prefix='/users')
    app.register_blueprint(rutasCuenta.main, url_prefix = '/accounts')
    app.register_blueprint(rutasMovimiento.main, url_prefix='/movements')

    return app