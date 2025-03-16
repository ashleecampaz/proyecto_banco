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
            'estado': self.estado
        }