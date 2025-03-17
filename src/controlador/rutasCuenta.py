from flask import Blueprint, render_template, redirect, url_for
from flask import request
from flask import jsonify
from src.modelo.Usuario import Usuario
from src.modelo.Cuenta import Cuenta
from ..datos import repositorio
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

@main.route('/registrar-cuenta/<int:cedula>',methods=['POST'])
def registrarCuentaform(cedula):
    saldo = request.form['monto']
    resultado = Cuenta.registrarCuenta(cedula=cedula, saldo=saldo)
    if resultado == True:
        mensaje ="Se agrego la cuenta correctamente"
    else:
        mensaje = "La cuenta no fue agregada"
    return render_template("cuentas.html",mensaje=mensaje, usuario='',cuentas=[])

@main.route('/listar/<int:cedula>',methods=['GET'])
def listarCuentas(cedula):
    Usuario_obj = Usuario.consultarUsuario(cedula)
    if not Usuario_obj:
        return jsonify({'message':'Usuario no encontrado'}), 404
    cuentas = Cuenta.listarCuentas(cedula)
    return cuentas, 200 

@main.route('/listar-cuentas',methods=['POST'])
def listarCuentasform():
    cedula = request.form['cedula']
    Usuario_obj = Usuario.consultarUsuario(cedula)
    if not Usuario_obj:
        mensaje = "Usuario no encontrado"
        return render_template("cuentas.html",mensaje=mensaje, usuario='',cuentas=[])
    cuentas = Cuenta.listarCuentas(cedula)
    mensaje = "El usuario fue encontrado"
    return render_template("cuentas.html",mensaje=mensaje, usuario=Usuario_obj, cuentas=cuentas)

@main.route('/consultar/<int:cuenta_id>',methods=['GET'])
def consultarCuenta(cuenta_id):
    cuenta = Cuenta.consultarCuenta(cuenta_id)
    if cuenta:
        return cuenta, 200
    return jsonify({'message':'Cuenta no encontrada'}), 404

@main.route('/actualizar/<int:cuenta_id>', methods=['PUT'])
def actualizarCuenta(cuenta_id):
    data = request.json
    resultado = repositorio.actualizarCuenta(cuenta_id, data.get("estado"), data.get("monto"))
    if resultado:
        return jsonify({"mensaje": "Cuenta actualizada correctamente"}), 200
    return jsonify({"error": "Cuenta no encontrada"}), 404

@main.route('/eliminar/<int:cuenta_id>', methods=['DELETE'])
def eliminarCuenta(cuenta_id):
    respuesta, codigo = repositorio.eliminarCuenta(cuenta_id)
    return jsonify(respuesta), codigo  

