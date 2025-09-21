\# Configuración de MongoDB



\## 1. Conectar a MongoDB



Abrir la terminal y ejecutar:



-monbash

-mongosh



Esto abre la consola interactiva de MongoDB.



2\. Crear y seleccionar la base de datos

Selecciona o crea la base de datos control\_gastos:



-use control\_gastos



\*Si la base de datos no existe, MongoDB la crea automáticamente.

\*Verifica la base de datos activa con:



-db



3\. Crear colecciones

Crea las colecciones necesarias:



-db.createCollection("usuarios")

-db.createCollection("transacciones")



Verifica que se crearon correctamente:



-show collections



Resultado esperado:



-usuarios

-transacciones



4\. Insertar usuario de prueba



db.usuarios.insertOne({

&nbsp; nombre: "Alejandro",

&nbsp; password: "1234",

&nbsp; email: "alejandro@example.com",

&nbsp; rol: "admin"

})



Para verificar que se insertó correctamente:



db.usuarios.find().pretty()

Resultado esperado:





{

&nbsp; "\_id": ObjectId("..."),

&nbsp; "nombre": "Alejandro",

&nbsp; "password": "1234",

&nbsp; "email": "alejandro@example.com",

&nbsp; "rol": "admin"

}

