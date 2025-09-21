\# Modelo de datos - MongoDB



\## Colecciones



\### usuarios

\- \_id: ObjectId

\- nombre: string

\- email: string

\- fecha\_creacion: date



\### transacciones

\- \_id: ObjectId

\- usuario\_id: ObjectId (referencia a usuarios)

\- descripcion: string

\- monto: float

\- tipo: "ingreso" | "gasto"

\- categoria: string (comida, transporte, hogar, etc.)

\- fecha: date



\## Relaciones

\- 1 usuario → N transacciones



