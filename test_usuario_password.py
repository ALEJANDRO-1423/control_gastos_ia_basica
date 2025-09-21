from app.controllers.usuarios_controller import crear_usuario, obtener_usuario
from bson.objectid import ObjectId

# Crear un usuario nuevo con contraseña
usuario_id = crear_usuario("Alejandro", "alejandro@mail.com", "1234")
print("Usuario creado con ID:", usuario_id)

# Consultar el usuario en la BD
usuario = obtener_usuario(usuario_id)
print("Documento completo en BD:")
print(usuario)
