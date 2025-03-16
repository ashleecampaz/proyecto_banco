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