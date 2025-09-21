\# Funcionalidad IA: Predicción de categoría de gasto



\## Descripción

Al registrar un gasto, el sistema intenta predecir automáticamente su categoría usando palabras clave.



\## Categorías disponibles

\- comida: restaurante, café, almuerzo, desayuno, cena

\- transporte: taxi, bus, metro, gasolina, uber

\- entretenimiento: cine, película, teatro, concierto, videojuego

\- hogar: supermercado, agua, luz, internet, renta

\- salud: farmacia, medicina, doctor, hospital

\- otros: si no coincide con ninguna categoría



\## Uso

\- La función `predecir\_categoria(descripcion)` recibe la descripción del gasto y devuelve la categoría sugerida.

\- Integrada en `crear\_transaccion()` para asignar automáticamente la categoría.



\## Ejemplo

```python

from app.controllers.transacciones\_controller import crear\_transaccion



id = crear\_transaccion("usuario\_id\_aqui", "Almuerzo en restaurante", 30.0, "gasto")


# Predicción de categoría de gasto

## Descripción
El sistema incluye una funcionalidad básica de **IA** que asigna automáticamente una categoría a un gasto en el momento en que se registra.  
La predicción se realiza buscando palabras clave dentro de la descripción de la transacción.

Si no se encuentra coincidencia con ninguna palabra clave, la transacción se clasifica como **"otros"**.

---

## Categorías iniciales
- **comida** → restaurante, café, almuerzo, desayuno, cena  
- **transporte** → taxi, bus, metro, gasolina, uber  
- **entretenimiento** → cine, película, teatro, concierto, videojuego  
- **hogar** → supermercado, agua, luz, internet, renta  
- **salud** → farmacia, medicina, doctor, hospital  
- **otros** → cualquier descripción que no coincida con las anteriores  

---

## Ejemplo de uso
**Entrada:**
"Almuerzo en restaurante"



**Salida:**
"comida"



---

## Integración en el sistema
- La función se encuentra en `app/ia_categoria.py`.
- Se invoca automáticamente en el CRUD de transacciones al crear un gasto.
- El resultado de la predicción se guarda en la base de datos en el campo **`categoria`** dentro de la colección `transacciones`.

Ejemplo de documento en MongoDB:


{
  "_id": ObjectId("..."),
  "usuario_id": "68cb5a16465d150faf86b01d",
  "descripcion": "Almuerzo en restaurante",
  "monto": 12.5,
  "tipo": "gasto",
  "categoria": "comida"
}



