from flask import Blueprint, render_template
from flask import jsonify
from src.modelo.Usuario import Usuario
main = Blueprint('inicio_blueprint',__name__)


@main.route('/Banco')
def inicio():
    usuarios = Usuario.listarUsuarios()
    return render_template('index.html',usuarios = usuarios)


@main.route('/consultar')
def consultarUsuarioform():
    mensaje = ""
    return render_template("usuarios.html", mensaje = mensaje, inactivo =True)

@main.route('/consultar-cuentas')
def consultarCuentasUsuarioform():
    mensaje = ""
    return render_template("cuentas.html", mensaje = mensaje, cuentas=[], usuario = '')