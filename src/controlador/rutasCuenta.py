from flask import Blueprint

main = Blueprint('cuentas_blueprint',__name__)


@main.route('/Cuenta')
def inicio():
    print('Cuenta')