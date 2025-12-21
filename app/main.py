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
     "nombre2": "NancyLoomis",
     "ghostfaces": 2,
    },
    {
     "pelicula_id": 3,
     "nombre1": "Roman Bridger",
     "ghostface": 1,
    },
    {
     "pelicula_id": 4,
     "nombre1": "Jill Roberts",
     "nombre2": "Charlie Walker",
     "ghostface": 2,
    },
    {
     "pelicula_id": 5,
     "nombre1": "Amber Freeman",
     "nombre2": "Richie",
     "ghostface": 2,
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
