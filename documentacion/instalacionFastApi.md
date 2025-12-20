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
