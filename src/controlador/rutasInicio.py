from flask import Blueprint
from flask import jsonify

main = Blueprint('inicio_blueprint',__name__)


@main.route('/Banco')
def inicio():
    reponse = jsonify({'message':'Success'})
    return reponse, 200