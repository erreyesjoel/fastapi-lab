# Modelos Pydantic
### Modelo Pydantic = Modelo de datos
## En que consiste un modelo de datos?
- Un modelo de datos es una estructura que define cómo debe ser un objeto:
qué campos tiene, qué tipo de datos acepta y cuáles son opcionales.
- En FastAPI, estos modelos se crean con Pydantic, y sirven para:
1. Validar automáticamente los datos que llegan a tu API
2. Mantener el código limpio y ordenado
3. Evitar funciones con demasiados parámetros
4. Generar documentación automática en Swagger
5. Asegurar que tus endpoints reciben datos correctos

**❌ Sin modelos de datos -> funciones largas y difíciles de mantener**
- Esto es lo que pasa cuando NO usas modelos de datos
```python
@app.post("/peliculas")
def crear_pelicula(
    pelicula_id: int,
    titulo: str,
    director: str,
    anio: int,
    genero: str,
    duracion: int,
    presupuesto: float,
    recaudacion: float,
    descripcion: str | None = None
):
    return {
        "pelicula_id": pelicula_id,
        "titulo": titulo,
        "director": director,
        "anio": anio,
        "genero": genero,
        "duracion": duracion,
        "presupuesto": presupuesto,
        "recaudacion": recaudacion,
        "descripcion": descripcion
    }
```
## Problemas:
1. La función se vuelve larga
2. Difícil de leer
3. Difícil de mantener
4. Swagger muestra demasiados parámetros sueltos
5. Si agregas un campo nuevo → tienes que modificar toda la función

**✅ Con modelos de datos (Pydantic) → código limpio y profesional**
- Primero defines un modelo
```python
from pydantic import BaseModel

class Pelicula(BaseModel):
    pelicula_id: int
    titulo: str
    director: str
    anio: int
    genero: str
    duracion: int
    presupuesto: float
    recaudacion: float
    descripcion: str | None = None
```
- Y el endpoint quedaría así:
```python
@app.post("/peliculas")
def crear_pelicula(peli: Pelicula):
    return peli
```
## Ventajas:
1. La función tiene un solo parámetro
2. Swagger muestra un JSON limpio
3. Validación automática
4. Si agregas un campo → solo lo añades al modelo
5. Mucho más fácil de mantener

## Resumen
**Un modelo Pydantic es una plantilla que define la estructura de un objeto**

**Sin modelos → funciones largas, desordenadas y difíciles de mantener**

**Con modelos → código limpio, validado y profesional**

**FastAPI usa estos modelos para generar Swagger automáticamente**
