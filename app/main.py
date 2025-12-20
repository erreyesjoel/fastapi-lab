from fastapi import FastAPI

app = FastAPI()

# ruta de prueba
@app.get('/')
def home():
    return "Hola mundo!"
