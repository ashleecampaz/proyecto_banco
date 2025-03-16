from ..datos import repositorio
from src.datos.repositorio import Cuenta
import random

class Cuenta():
    def __init__(self, cuenta_id, usuario_cedula, monto, estado):
        self.cuenta_id = cuenta_id
        self.usuario_cedula = usuario_cedula
        self.monto = monto
        self.estado = estado
    
    def to_json(self):
        return {
            'cuenta_id': self.cuenta_id,
            'usuario_cedula':self.usuario_cedula,
            'monto':self.monto,
            'estado':self.estado
        }
    @staticmethod
    def generar_numero_cuenta():
        """Genera un número de cuenta único"""
        while True:
            numero = str(random.randint(100000000000000, 999999999999999))  # Número de 15 dígitos
            if not repositorio.consultarCuenta(numero):
                return numero
    @classmethod
    def registrarCuenta(cls, cedula, saldo):
        cuenta_id=cls.generar_numero_cuenta()
        return repositorio.agregarCuenta(cuenta_id,cedula, saldo, 'activo')
    @classmethod
    def listarCuentas(cls, cedula):
        cuentas = repositorio.consultarCuentas(cedula)
        cuentas_json = []
        for cu in cuentas:
            cuentas_json.append(cu.to_json())
        return cuentas_json
    @classmethod
    def consultarCuenta(cls, cuenta_id):
        cuenta = repositorio.consultarCuenta(cuenta_id)
        return cuenta.to_json() if cuenta else None