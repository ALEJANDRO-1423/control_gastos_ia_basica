from app.controllers.transacciones_controller import crear_transaccion, listar_transacciones

# Simulamos un usuario existente (cambia el ID por el tuyo de MongoDB si es necesario)
usuario_id = "usuario_id_aqui"

# Crear transacciones sin categoría (la IA la predice)
crear_transaccion(usuario_id, "Almuerzo en restaurante", 30.0, "gasto")
crear_transaccion(usuario_id, "Taxi a casa", 15.0, "gasto")
crear_transaccion(usuario_id, "Cine con amigos", 20.0, "gasto")

# Crear una transacción con categoría explícita (no usa IA)
crear_transaccion(usuario_id, "Compra en tienda", 50.0, "gasto", categoria="hogar")

# Listar todas las transacciones y ver categorías
for t in listar_transacciones():
    print(t)
