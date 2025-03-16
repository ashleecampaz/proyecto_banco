from flask import Blueprint
from flask import request
from flask import jsonify
from src.modelo.Usuario import Usuario
from ..datos import repositorio
main = Blueprint('usuario_blueprint',__name__)


@main.route('/registrar',methods=['POST'])
def registrarUsuario():
    cedula = request.json['cedula']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    celular =  request.json['celular']
    
    resultado = Usuario.registrarUsuario(cedula=cedula, nombre=nombre, apellido=apellido, celular=celular)
    if resultado == True:
        reponse = jsonify({'message':'Success'})
        return reponse, 200
    reponse = jsonify({'message':'Failed'})
    return reponse, 500
    


@main.route('/listar',methods=['GET'])
def listarUsuarios():
   usuarios = Usuario.listarUsuarios()
   return usuarios, 200

@main.route('/consultar/<int:cedula>',methods=['GET'])
def consultarUsuario(cedula):
    usuario = Usuario.consultarUsuario(cedula)
    if usuario:
        return usuario, 200
    return jsonify({'message':'Usuario no encontrado'}), 404

@main.route('/actualizar/<int:cedula>', methods=['PUT'])
def actualizar_usuario(cedula):
    data = request.json
    resultado = repositorio.actualizarUsuario(cedula, data.get("nombre"), data.get("apellido"), data.get("celular"))
    if resultado:
        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@main.route('/eliminar/<int:cedula>', methods=['DELETE'])
def eliminar_usuario(cedula):
    resultado = repositorio.eliminarUsuario(cedula)
    if resultado:
        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404