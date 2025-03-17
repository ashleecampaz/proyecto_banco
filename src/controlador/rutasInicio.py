from flask import Blueprint, render_template
from flask import jsonify
from src.modelo.Usuario import Usuario
main = Blueprint('inicio_blueprint',__name__)


@main.route('/Banco')
def inicio():
    reponse = jsonify({'message':'Success'})
    usuarios = Usuario.listarUsuarios()
    cadena_usuarios =[]
    for us in usuarios:
        cadena_usuarios.append(f"{us["nombre"]} {us["apellido"]}")
    return render_template('index.html',usuarios = cadena_usuarios)


@main.route('/consultar')
def consultarUsuarioform():
    mensaje = ""
    return render_template("usuarios.html", mensaje = mensaje)