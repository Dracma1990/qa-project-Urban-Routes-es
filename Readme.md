Nombre del Proyecto: Proyecto Sprint 8 Andrés Vargas
Descripción del Proyecto: Automatización de pruebas de una aplicación web
Tecnologías y técnicas utilizadas: GitHub y Pycharm. Vínculo entre repositorios locales y remotos.
Cómo ejecutar las pruebas: 
Cómo Ejecutar el Proyecto

### 1. Clona el Repositorio

Abre tu terminal y navega al directorio donde desees guardar el proyecto:

```bash
cd ~/projects
git clone git@github.com:TU_USUARIO/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es

2. Configura la URL del Servidor
Abre el archivo data.py y reemplaza la URL base con tu propia URL generada por TripleTen (ejemplo: https://cnt-xxx.containerhub.tripleten-services.com?lng=es).

# data.py
BASE_URL = "https://TU_URL.containerhub.tripleten-services.com?lng=es"

3. Instala las Dependencias
Asegúrate de tener pip instalado, luego ejecuta:
pip install -r requirements.txt
Si no hay un requirements.txt, instala Selenium manualmente:
pip install selenium

4. Ejecuta las Pruebas
Desde el directorio raíz del proyecto:
pytest main.py
Esto ejecutará las pruebas automatizadas definidas en main.py.

Pruebas Automatizadas Incluidas
Las pruebas cubren:
Ingreso de dirección de origen y destino.
Selección de tarifa Comfort.
Ingreso de número de teléfono.
Agregado de tarjeta de crédito (incluye detección del CVV y confirmación con código).
Envío de mensaje al conductor.
Peticiones adicionales (manta, pañuelos, helado).
Validación del modal de búsqueda y del conductor asignado
