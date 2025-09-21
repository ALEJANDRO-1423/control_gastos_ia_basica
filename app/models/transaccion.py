class Transaccion:
    def __init__(self, usuario_id, descripcion, monto, tipo):
        self.usuario_id = usuario_id
        self.descripcion = descripcion
        self.monto = monto
        self.tipo = tipo  # "ingreso" o "gasto"

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "descripcion": self.descripcion,
            "monto": self.monto,
            "tipo": self.tipo
        }
