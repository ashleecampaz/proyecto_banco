from flask import Blueprint, render_template, redirect, url_for
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
    

@main.route('/registrar-form',methods=['POST'])
def registrarUsuarioform():
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    celular =  request.form['celular']
    
    resultado = Usuario.registrarUsuario(cedula=cedula, nombre=nombre, apellido=apellido, celular=celular)
    return redirect(url_for('inicio_blueprint.inicio'))

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

@main.route('/consultar-usuario',methods=['POST'])
def consultarUsuarioform():
    cedula = request.form['cedula']
    usuario = Usuario.consultarUsuario(cedula)
    if usuario:
        mensaje = "El usuario fue encontrado!"
        return render_template("usuarios.html",nombre = usuario["nombre"], apellido= usuario["apellido"],
                               celular = usuario["celular"], cedula=usuario["cedula"], mensaje = mensaje, inactivo=False)
    mensaje = "El usuario no fue encontrado"
    return render_template("usuarios.html", mensaje = mensaje, inactivo=True)

@main.route('/actualizar/<int:cedula>', methods=['PUT'])
def actualizarUsuario(cedula):
    data = request.json
    resultado = Usuario.actualizarUsuario(cedula, data.get("nombre"), data.get("apellido"), data.get("celular"))
    if resultado:
        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@main.route('/actualizar-usuario', methods=['POST'])
def actualizarUsuarioform():

    accion = request.form.get("accion")
  
    cedula = request.form['cedula']
    if accion == "eliminar":
        
        return eliminarUsuarioform(cedula)
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    celular =  request.form['celular']

    resultado = Usuario.actualizarUsuario(cedula, nombre=nombre, apellido=apellido, celular=celular)
    if resultado:
        mensaje = "El usuario fue actualizado correctamente"
    else:  
        mensaje = "El usuario no fue actualizado"
    return render_template("usuarios.html", mensaje = mensaje, inactivo=True)

@main.route('/eliminar/<int:cedula>', methods=['DELETE'])
def eliminarUsuario(cedula):
    resultado = Usuario.eliminarUsuario(cedula)
    if resultado:
        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@main.route('/eliminar', methods=['POST'])
def eliminarUsuarioform(cedula):
    resultado = Usuario.eliminarUsuario(cedula)
    if resultado:
        mensaje = "el usuario fue eliminado correctamente"
    else:
        mensaje = "El usuario no fue eliminado"
    return render_template("usuarios.html", mensaje = mensaje, inactivo=True)