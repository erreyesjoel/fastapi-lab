**# Modelos Pydantic
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

# NOTA
- En nuestro Swagger, veremos nuestro modelo de datos o Pydantic en el apartado de 'Schemas'**
- Incluye: Tipos de datos, campos opcionales, validaciones, descripciones...
# ✔️ Validaciones de datos con Pydantic**
- Los modelos Pydantic no solo definen la estructura también permiten validar los datos automáticamente.
- FastAPI usa estas validaciones para:
1. Rechazar datos incorrectos
2. Mostrar errores claros en Swagger
3. Asegurar que tu API recibe valores válidos
- Ejemplo de validaciones
```python
from pydantic import BaseModel, Field

class Pelicula(BaseModel):
    pelicula_id: int = Field(gt=0, description="Debe ser un número mayor que 0")
    titulo: str = Field(min_length=1, max_length=50)
    director: str = Field(min_length=1)
    anio: int = Field(ge=1900, le=2100)
    genero: str
    duracion: int = Field(gt=0)
    presupuesto: float = Field(ge=0)
    recaudacion: float = Field(ge=0)
    descripcion: str | None = Field(default=None, max_length=200)
```
### ¿Qué validaciones estamos aplicando?
- gt=0 → mayor que 0
- ge=0 → mayor o igual que 0
- min_length / max_length → longitud mínima y máxima
- description → aparece en Swagger
- default=None → campo opcional

### ¿Qué pasa si envías datos incorrectos?
- FastAPI devuelve un error automático:
1. Tipo incorrecto
2. Campo faltante
3. Valor fuera de rango
4. Texto demasiado largo
5. Número negativo donde no debe

Todo esto sin que tú escribas lógica de validación.

### Resumen
- Un modelo Pydantic define la estructura de un objeto.
- También define validaciones automáticas.
- Swagger muestra estas validaciones en el esquema.
- Si envías datos incorrectos → FastAPI los rechaza.
- Esto hace tu API más segura, limpia y profesional.
