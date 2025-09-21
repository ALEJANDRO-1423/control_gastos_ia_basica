from app.controllers.transacciones_controller import crear_transaccion, listar_transacciones

# Reemplaza con el ID de un usuario que exista en tu DB
usuario_id = "TU_ID_DE_USUARIO_AQUI"

# Crear una transacción de prueba
transaccion_id = crear_transaccion(usuario_id, "Almuerzo en restaurante", 12.5)

print("Transacción creada con ID:", transaccion_id)

# Listar todas las transacciones para verificar
transacciones = listar_transacciones()
for t in transacciones:
    print(t)
