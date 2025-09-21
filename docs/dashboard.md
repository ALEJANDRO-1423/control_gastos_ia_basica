Dashboard

## Descripción
El dashboard permite visualizar un resumen de los usuarios, sus balances y alertas.

### 1. Cálculo del balance
- Se calcula por usuario como:
Balance = suma de ingresos - suma de gastos


- Se recorre la colección de transacciones y se suman los montos según el tipo ("ingreso" o "gasto").

### 2. Generación de alertas
- Se generan alertas cuando el total de gastos de un usuario supera un límite definido (por defecto 100).  
- Ejemplo de alerta:
Alerta: Has gastado 120, superando el límite de 100



### 3. Ejemplo de salida del dashboard

Usuario: Alejandro (alejandro@example.com)
Balance: -5.0
No hay alertas.



Si un usuario supera el límite de gasto, se mostrará algo como:

Usuario: Alejandro (alejandro@example.com)
Balance: -150.0
Alertas:

Alerta: Has gastado 150, superando el límite de 100


### 4. Uso
- Se utiliza la función `mostrar_dashboard()` desde `dashboard_controller.py` para imprimir el dashboard completo en consola

