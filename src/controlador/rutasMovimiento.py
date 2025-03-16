from flask import Blueprint

main = Blueprint('movimientos_blueprint',__name__)


@main.route('/Movimientos')
def inicio():
    print('movimiento')