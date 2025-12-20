# Instalacion del entorno fast api
1. Crear entorno virtual, ya sea venv o env
```bash
python3 -m venv venv
```
- Salida del terminal, entorno venv creado exitosamente
```bash
joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$ ls 
documentacion  README.md  venv
joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$ ls venv/
bin  include  lib  lib64  pyvenv.cfg
joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$  
```
2. Activar o habilitar el entorno virtual, y ya podremos instalar los modulos, etc
```bash
source venv/bin/activate
```
- Los modulos que necesitamos inicialmente para crear una "aplicacion" fastApi son
**Modulo de fastapi y uvicorn, que es quien ejecuta la app de fastapi**

3. Instalacion de fastapi y uvicorn
```bash
(venv) joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$ pip install fastapi uvicorn
```
- Ya de paso generamos el fichero requirements.txt
```bash
(venv) joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$ pip freeze > requirements.txt 
```
## NOTA
- pip install -r requirements.txt -> Instala todas las dependencias listadas en el archivo requirements.txt

4. Donde guardaré main.py
```bash
(venv) joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$ mkdir app
(venv) joel-erreyes:~/docsjoel/proyectos personales/fastapi-lab$ touch app/main.py
```
5. Crear la aplicacion como tal en main.py
- En principio con esto ya la tenemos creada, y ya podremos ir haciendo rutas
```python
from fastapi import FastAPI

app = FastAPI()
```
6. Definimos una ruta de prueba
```python
from fastapi import FastAPI

app = FastAPI()

# ruta de prueba
@app.get('/')
def home():
    return "Hola mundo!"
```
- Para ejecutar y poder ver nuestra api en web local
```bash
uvicorn main:app 
```
- Pero como yo tengo el puerto 8000 ocupado, lo hago con el 8002
```bash
uvicorn main:app --reload --port 8002
```
- Si vamos a http://127.0.0.1:8002/
- Nos devuelve un hola mundo
