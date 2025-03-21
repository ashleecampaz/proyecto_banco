from ..datos import repositorio
from src.datos.repositorio import Usuario
class Usuario():
    def __init__(self, cedula, nombre, apellido, celular):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
    
    def to_json(self):
        return {
            'cedula': self.cedula,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'celular': self.celular
        }
    
    @classmethod
    def registrarUsuario(cls, cedula, nombre, apellido, celular):
        return repositorio.agregarUsuario(cedula, nombre, apellido, celular)
    
    @classmethod
    def listarUsuarios(cls):
        usuarios = repositorio.consultarUsuarios()
        usuarios_json = []
        for us in usuarios:
             usuarios_json.append(us.to_json())
        return usuarios_json
    @classmethod
    def consultarUsuario(cls, cedula):
        usuario = repositorio.consultarUsuario(cedula)
        return usuario.to_json() if usuario else None
    @classmethod
    def actualizarUsuario(cls, cedula, nombre=None, apellido=None, celular=None):
        exito = repositorio.actualizarUsuario(cedula, nombre, apellido, celular)
        return {'mensaje': 'Usuario actualizado exitosamente'} if exito else {'error': 'Usuario no encontrado'}
    @classmethod
    def eliminarUsuario(cls, cedula):
        exito = repositorio.eliminarUsuario(cedula)
        return {'mensaje': 'Usuario eliminado exitosamente'} if exito else {'error': 'Usuario no encontrado'}    
