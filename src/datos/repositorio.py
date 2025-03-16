from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
import random
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# One-to-Many Relationship: Parent has many Children
class Usuario(db.Model):
    cedula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(100), nullable=False)
   
    cuenta = db.relationship('Cuenta', backref='usuario', lazy=True)
    def to_json(self):
        return {
            'cedula': self.cedula,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'celular': self.celular
        }

class Cuenta(db.Model):
    cuenta_id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(15), default='activo', nullable=False)
    monto= db.Column(db.Integer, default=0,nullable=False)

    usuario_cedula = db.Column(db.Integer, db.ForeignKey('usuario.cedula'))
    movimiento = db.relationship('Movimiento', backref='cuenta', lazy=True, cascade="all, delete-orphan")
    def to_json(self):
        return {
            'cuenta_id': self.cuenta_id,
            'usuario_cedula':self.usuario_cedula,
            'monto':self.monto,
            'estado': self.estado
        }


class Movimiento(db.Model):
    movimiento_id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(30), nullable=False)
    monto= db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, default=func.now())
     
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.cuenta_id'))

#Crea la base de datos
with app.app_context():
    db.create_all()

def agregarUsuario(cedula, nombre, apellido, celular):
    with app.app_context():
        try:
            usuario = Usuario(cedula= cedula, nombre=nombre, apellido = apellido, celular=celular)
            db.session.add(usuario)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
             db.session.rollback()  # Revierte cambios si hay un error
             return False
        

def agregarCuenta(cuenta_id,usuario_cedula,monto,estado):
    with app.app_context():
        try:
            Usuario_obj = Usuario.query.filter_by(cedula=usuario_cedula).first()
            if not Usuario_obj:
                return False
            cuenta = Cuenta(cuenta_id=cuenta_id,usuario_cedula=usuario_cedula,monto=monto,estado=estado)
            db.session.add(cuenta)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
             db.session.rollback()  # Revierte cambios si hay un error
             return False
    

def consultarUsuarios():
    with app.app_context():
        padres = Usuario.query.all()
        return padres
def consultarUsuario(cedula):
    with app.app_context():
        usuario = Usuario.query.filter_by(cedula=cedula).first()
        return usuario
def consultarCuentas(cedula):
    with app.app_context():
        cuentas = Cuenta.query.filter_by(usuario_cedula=cedula).all()
        return cuentas
def consultarCuenta(cuenta_id):
    with app.app_context():
        cuenta = Cuenta.query.filter_by(cuenta_id=cuenta_id).first()
        return cuenta