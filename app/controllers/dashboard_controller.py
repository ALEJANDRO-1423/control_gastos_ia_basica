from app.controllers.usuarios_controller import listar_usuarios
from app.controllers.transacciones_controller import listar_transacciones

# Función para calcular balance por usuario
def calcular_balance(usuario_id):
    transacciones = listar_transacciones()
    balance = 0
    for t in transacciones:
        if t["usuario_id"] == usuario_id:
            if t["tipo"] == "ingreso":
                balance += t["monto"]
            elif t["tipo"] == "gasto":
                balance -= t["monto"]
    return balance

# Función para generar alertas
def generar_alertas(usuario_id, limite_gasto=100):
    transacciones = listar_transacciones()
    alertas = []
    total_gastos = sum(
        t["monto"] for t in transacciones 
        if t["usuario_id"] == usuario_id and t["tipo"] == "gasto"
    )
    
    if total_gastos > limite_gasto:
        alertas.append(
            f"Alerta: Has gastado {total_gastos}, superando el límite de {limite_gasto}"
        )
    
    return alertas

# Función para mostrar dashboard completo
def mostrar_dashboard():
    usuarios = listar_usuarios()
    for u in usuarios:
        uid = str(u["_id"])
        print(f"\nUsuario: {u['nombre']} ({u['email']})")
        balance = calcular_balance(uid)
        print(f"Balance: {balance}")
        alertas = generar_alertas(uid)
        if alertas:
            print("Alertas:")
            for a in alertas:
                print(" -", a)
        else:
            print("No hay alertas.")
