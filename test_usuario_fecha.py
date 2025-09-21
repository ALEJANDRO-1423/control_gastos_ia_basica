from app.controllers.usuarios_controller import crear_usuario, obtener_usuario, listar_usuarios

# Intentar crear un usuario nuevo
uid = crear_usuario("Alejandro Avila", "alejandro@mail.com")
print("Usuario ID:", uid)

# Recuperar y mostrar el documento entero
u = obtener_usuario(uid)
print("Documento en BD:", u)

# Listar usuarios (muestra fecha_creacion)
for user in listar_usuarios():
    print(user)
