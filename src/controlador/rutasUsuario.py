from flask import Blueprint
from flask import request
from flask import jsonify
from src.modelo.Usuario import Usuario
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