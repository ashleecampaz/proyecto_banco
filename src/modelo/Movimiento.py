from ..datos import repositorio
from datetime import datetime
import random

class Movimiento():
    def __init__(self, movimiento_id, cuenta_id, tipo, monto, fecha):
        self.movimiento_id = movimiento_id
        self.cuenta_id = cuenta_id
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha
    
    def to_json(self):
        return {
            'movimiento_id': self.movimiento_id,
            'cuenta_id':self.cuenta_id,
            'tipo':self.tipo,
            'monto': self.monto,
            'fecha': self.fecha
        }
    @staticmethod
    def generar_numero_cuenta():
        """Genera un número de cuenta único"""
        while True:
            numero = str(random.randint(100000000000000, 999999999999999))  # Número de 15 dígitos
            if not repositorio.consultarMovimiento(numero):
                return numero
    @classmethod
    def registrarMovimiento(cls, cuenta_id, tipo, monto):
        movimiento_id=cls.generar_numero_cuenta()
        return repositorio.agregarMovimiento(movimiento_id,cuenta_id, tipo, monto, datetime.now())
    @classmethod
    def listarMovimientos(cls, cuenta_id):
        movimientos = repositorio.consultarMovimientos(cuenta_id)
        movimientos_json = []
        for mo in movimientos:
            movimientos_json.append(mo.to_json())
        return movimientos_json
    @classmethod
    def consultarMovimiento(cls, movimiento_id):
        movimiento = repositorio.consultarMovimiento(movimiento_id)
        return movimiento.to_json() if movimiento else None
    @classmethod
    def actualizarMovimiento(cls, movimiento_id, tipo=None, monto=None):
        exito = repositorio.actualizarMovimiento(movimiento_id, tipo, monto)
        return {'mensaje': 'Movimiento actualizado exitosamente'} if exito else {'error': 'Movimiento no encontrado'}
    @classmethod
    def eliminarMovimiento(cls, movimiento_id):
        exito = repositorio.eliminarMovimiento(movimiento_id)
        return {'mensaje': 'Movimiento eliminado exitosamente'} if exito else {'error': 'Movimiento no encontrado'}