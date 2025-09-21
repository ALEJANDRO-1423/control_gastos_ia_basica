from app.controllers.usuarios_controller import crear_usuario, listar_usuarios

# Crear usuario de prueba
crear_usuario("Prueba", "prueba@mail.com", "1234")

# Listar usuarios
usuarios = listar_usuarios()
for u in usuarios:
    print(u)
