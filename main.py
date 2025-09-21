from app.controllers.usuarios_controller import crear_usuario
from app.controllers.transacciones_controller import crear_transaccion, obtener_transaccion

# 1) Crear usuario de prueba (retorna el ID como string)
usuario_id = crear_usuario("Alejandro", "alejandro@mail.com")
print("Usuario creado con ID:", usuario_id)

# 2) Crear transacción (sin categoría explícita) — la IA predice "comida"
transaccion_id = crear_transaccion(usuario_id, "Almuerzo en restaurante", 12.5)
print("Transacción creada con ID:", transaccion_id)

# 3) Recuperar la transacción desde la BD y mostrarla (incluye la categoría predicha)
transaccion = obtener_transaccion(transaccion_id)
print("Transacción creada con predicción de categoría:")
print(transaccion)

