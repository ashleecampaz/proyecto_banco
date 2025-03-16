from flask import request
from flask import jsonify
from src.modelo.Usuario import Usuario
from src.modelo.Cuenta import Cuenta
from flask import Blueprint

main = Blueprint('cuentas_blueprint',__name__)
@main.route('/registrar',methods=['POST'])
def registrarCuenta():
    cedula = request.json['cedula']
    saldo = request.json['monto']
    resultado = Cuenta.registrarCuenta(cedula=cedula, saldo=saldo)
    if resultado == True:
        reponse = jsonify({'message':'Success'})
        return reponse, 200
    reponse = jsonify({'message':'Failed'})
    return reponse, 500

@main.route('/listar/<int:cedula>',methods=['GET'])
def listarCuentas(cedula):
    Usuario_obj = Usuario.consultarUsuario(cedula)
    if not Usuario_obj:
        return jsonify({'message':'Usuario no encontrado'}), 404
    cuentas = Cuenta.listarCuentas(cedula)
    return cuentas, 200 

@main.route('/consultar/<int:cuenta_id>',methods=['GET'])
def consultarCuenta(cuenta_id):
    cuenta = Cuenta.consultarCuenta(cuenta_id)
    if cuenta:
        return cuenta, 200
    return jsonify({'message':'Cuenta no encontrada'}), 404

    

