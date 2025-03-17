from flask import Blueprint
from flask import Blueprint, request, jsonify
from src.modelo.Movimiento import Movimiento
from src.modelo.Cuenta import Cuenta
from ..datos import repositorio
main = Blueprint('movimientos_blueprint',__name__)


@main.route('/registrar',methods=['POST'])
def registrarMovimiento():
    try:
        datos = request.get_json()
        print("Datos recibidos:", datos)  
        cuenta_id = datos["cuenta_id"]
        tipo = datos["tipo"]
        monto = datos["monto"]        
        resultado = Movimiento.registrarMovimiento(cuenta_id=cuenta_id, tipo=tipo, monto=monto)        
        return jsonify({"message": "Success"}), 200
    except Exception as e:
        print("Error:", e)  
        return jsonify({"message": "Failed"}), 500
@main.route('/listar/<int:cuenta_id>',methods=['GET'])
def listarMovimientos(cuenta_id):
    cuenta_obj = Cuenta.consultarCuenta(cuenta_id)
    if not cuenta_obj:
        return jsonify({'message':'Cuenta no encontrada'}), 404
    movimientos = Movimiento.listarMovimientos(cuenta_id)
    return movimientos, 200
@main.route('/consultar/<int:movimiento_id>',methods=['GET'])
def consultarMovimiento(movimiento_id):
    movimiento = Movimiento.consultarMovimiento(movimiento_id)
    if movimiento:
        return movimiento, 200
    return jsonify({'message':'Movimiento no encontrado'}), 404
    
@main.route('/actualizar/<int:movimiento_id>', methods=['PUT'])
def actualizarMovimiento(movimiento_id):
    data = request.json
    resultado = Movimiento.actualizarMovimiento(movimiento_id, data.get("tipo"), data.get("monto"))
    if resultado:
        return jsonify({"mensaje": "Movimiento actualizado correctamente"}), 200
    return jsonify({"error": "Movimiento no encontrado"}), 404

@main.route('/eliminar/<int:movimiento_id>', methods=['DELETE'])
def eliminarMovimiento(movimiento_id):
    resultado = Movimiento.eliminarMovimiento(movimiento_id)
    if resultado:
        return jsonify({"mensaje": "Movimiento eliminado correctamente"}), 200
    return jsonify({"error": "Movimiento no encontrado"}), 404