from fastapi import FastAPI

app = FastAPI()

# ruta de prueba
@app.get('/')
def home():
    return "Hola mundo!"
# array para devolver una api sencilla, la haré de los ghostface de las peliculas de Scream
# id hará referencia al numero de pelicula que es, scream1, scream2...
arrayGhostfaces = [
    {
     "pelicula_id": 1,
     "nombre1": "Billy Loomis",
     "nombre2": "Stu",
     "ghostfaces": 2,
    },
    {
     "pelicula_id": 2,
     "nombre1": "Mickey Altieri",
     "nombre2": "Nancy Loomis",
     "ghostfaces": 2,
    },
    {
     "pelicula_id": 3,
     "nombre1": "Roman Bridger",
     "ghostfaces": 1,
    },
    {
     "pelicula_id": 4,
     "nombre1": "Jill Roberts",
     "nombre2": "Charlie Walker",
     "ghostfaces": 2,
    },
    {
     "pelicula_id": 5,
     "nombre1": "Amber Freeman",
     "nombre2": "Richie",
     "ghostfaces": 2,
    },
]
@app.get('/scream-ghostfaces/{pelicula_id}')
def ghostfaces(pelicula_id: int): # debemos indicar el tipo que pasamos por la url, pasamos un id, entonces int, asi no hay confusiones y nuestra api funcionará
    for ghostface in arrayGhostfaces : # bucle para devolverlos, le damos nombre ghostface que recorre el array -> arrayGhostfaces
        if ghostface["pelicula_id"] == pelicula_id: # comprobamos si el id de la película coincide con el que llega por la URL
            return ghostface # devolvemos el ghostface, NO EL ARRAY COMPLETO
    return {"error": "Ghostface no encontrado"}

@app.get('/scream-ghostfaces') # en esta api, DEVOLVEMOS TODOS LOS GHOSTFACES
def devolverGhostfaces():
    return arrayGhostfaces

# Querystring: devolver las películas de Scream según el número de ghostfaces que tienen
@app.get('/ghostfaces')
def queryGhostfaces(ghostfaces: int):
    resultados = []  # lista vacía donde guardaremos las películas que coincidan
    # Recorremos todas las películas del array
    for peli in arrayGhostfaces:
        # Si el número de ghostfaces de la película coincide con el parámetro recibido...
        if peli.get('ghostfaces') == ghostfaces:
            resultados.append(peli)  # ...la añadimos a la lista de resultados
    return resultados  # devolvemos todas las coincidencias

# API POST de prueba: añadir una nueva película/ghostface al array en memoria
@app.post('/scream1')
# En Python, los parámetros obligatorios van primero; los opcionales (con valor por defecto) al final
def scream1Ghostfaces(pelicula_id: int, nombre1: str, ghostfaces: int, nombre2: str | None = None):
    # Creamos el diccionario con los datos recibidos (simulando un registro, ya que no hay base de datos)
    nuevo = {
        'pelicula_id': pelicula_id,
        'nombre1': nombre1,
        'nombre2': nombre2,  # Puede ser None si no se envía
        'ghostfaces': ghostfaces
    }
    # Guardamos el nuevo registro en el array en memoria
    arrayGhostfaces.append(nuevo)
    # Devolvemos el objeto creado como respuesta
    return nuevo
