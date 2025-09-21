\# CRUD de Usuarios



\## Ejemplo de uso



```python

from app.controllers.usuarios\_controller import crear\_usuario, obtener\_usuario, actualizar\_usuario, eliminar\_usuario, listar\_usuarios



\# Crear usuario

usuario\_id = crear\_usuario("Alejandro", "alejandro@example.com")

print("Usuario creado con ID:", usuario\_id)



\# Obtener usuario

usuario = obtener\_usuario(usuario\_id)

print("Datos del usuario:", usuario)



\# Actualizar usuario

actualizar\_usuario(usuario\_id, nombre="Alejandro A.")

usuario = obtener\_usuario(usuario\_id)

print("Usuario actualizado:", usuario)



\# Listar todos los usuarios

usuarios = listar\_usuarios()

print("Lista de usuarios:", usuarios)



\# Eliminar usuario

eliminar\_usuario(usuario\_id)

print("Usuario eliminado")



