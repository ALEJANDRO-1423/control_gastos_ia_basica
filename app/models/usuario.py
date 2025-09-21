from datetime import datetime

class Usuario:
    def __init__(self, nombre, email, password, fecha_creacion: datetime = None):
        self.nombre = nombre
        self.email = email
        self.password = password  # nuevo campo
        # Guardamos la fecha de creación (UTC). Si no se proporciona, usamos ahora.
        self.fecha_creacion = fecha_creacion or datetime.utcnow()

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password,  # guardar en la BD
            "fecha_creacion": self.fecha_creacion
        }
