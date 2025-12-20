## 📄 Documentación automática de FastAPI

FastAPI genera documentación automática de la API sin necesidad de configurar nada adicional.  
Esto es posible gracias a **OpenAPI**, que describe los endpoints, parámetros, modelos y respuestas.

FastAPI incluye dos interfaces de documentación:

---

### ✅ `/docs` — Swagger UI

- Es la interfaz interactiva por defecto.
- Permite probar los endpoints directamente desde el navegador.
- Muestra parámetros, respuestas, códigos de estado y modelos.
- Muy útil durante el desarrollo.

Puedes acceder a ella en:

http://127.0.0.1:8002/docs


(o el puerto que estés usando)

---

### ✅ `/redoc` — ReDoc

- Es otra interfaz de documentación generada automáticamente.
- Más limpia y orientada a lectura técnica.
- No es interactiva como Swagger, pero es muy clara para revisar la estructura de la API.

Disponible en:

http://127.0.0.1:8002/redoc


---

### ✅ ¿Por qué existe esta documentación automática?

FastAPI utiliza **OpenAPI** para generar:

- Esquemas de datos
- Validaciones
- Ejemplos
- Documentación de rutas
- Tipos de respuesta

Esto permite que la API esté documentada desde el primer momento sin esfuerzo adicional.

---

### ✅ Personalizar la documentación (opcional)

Puedes cambiar el título, descripción o desactivar Swagger/ReDoc desde la creación de la app:

```python
app = FastAPI(
    title="Mi API con FastAPI",
    description="Documentación automática generada por FastAPI",
    version="1.0.0",
    docs_url="/documentacion",
    redoc_url="/redoc-custom"
)
