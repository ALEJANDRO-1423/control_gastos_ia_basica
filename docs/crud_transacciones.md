\# CRUD de Transacciones



\## Ejemplo de uso



```python

from app.controllers.transacciones\_controller import (

&nbsp;   crear\_transaccion, obtener\_transaccion, actualizar\_transaccion,

&nbsp;   eliminar\_transaccion, listar\_transacciones

)



\# Crear transacción

transaccion\_id = crear\_transaccion("usuario\_id\_aqui", "Compra de libros", 50000, "gasto")

print("Transacción creada con ID:", transaccion\_id)



\# Obtener transacción

transaccion = obtener\_transaccion(transaccion\_id)

print("Datos de la transacción:", transaccion)



\# Actualizar transacción

actualizar\_transaccion(transaccion\_id, descripcion="Compra de libros y útiles")

transaccion = obtener\_transaccion(transaccion\_id)

print("Transacción actualizada:", transaccion)



\# Listar todas las transacciones

transacciones = listar\_transacciones()

print("Lista de transacciones:", transacciones)



\# Eliminar transacción

eliminar\_transaccion(transaccion\_id)

print("Transacción eliminada")



