from app.controllers.transacciones_controller import crear_transaccion, listar_transacciones

# Crear transacciones de prueba
id1 = crear_transaccion("usuario_id_aqui", "Almuerzo en restaurante", 30.0, "gasto")
id2 = crear_transaccion("usuario_id_aqui", "Taxi a casa", 15.0, "gasto")
id3 = crear_transaccion("usuario_id_aqui", "Cine con amigos", 20.0, "gasto")

# Listar todas las transacciones y ver categorías
transacciones = listar_transacciones()
for t in transacciones:
    print(t)
