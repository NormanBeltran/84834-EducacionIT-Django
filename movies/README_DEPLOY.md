# Receta para el despliegue en la nube: PythonAnywhere

- Registarse en https://www.pythonanywhere.com/ para obtener recursos de PythonAnywhere

## Pasos

- ZIP del proyecto que desarrollamos
- Loguearnos en PythonAnywhere
- Creamos en Web un Proyecto de tipo Django y elegimos la última versión de Python
- En Files --> Upload file y subimos el archivo zipeado
- En consola elegimos Bash para ingresar en la terminal de Linux de la VM que nos dio PythonAnywhere
- ls -l nos muestra todos los archivos y carpetas que tenemos en la carpeta donde estamos parados
- pwd muestra la carpeta donde estoy parado
- cd nombre_carpeta change directory a la carpeta correspondiente
- en /home/usuario ejecutar rm -r movies (esto elimina laa carpeta que creo PythonAnywhere cuando creamos el proyecto)
- clear (limpiamos la pantalla)
- unzip movies.zip (descompactamos todos los archivos del zip)

- En Files abrimos el archivo settings.py
    - DEBUG = False
    - ALLOWED_HOSTS = ["*"]
    - STATIC_ROOT = BASE_DIR / 'static'

- En la consola, dentro de la carpeta movies ejecutamos:
    - python manage.py collectstatic    

## Para desplegar en PythonAnywhere pero en una BD MySQL
- En Databases de PythonAnywhere crear la BD y la contraseña de acceso
- En settings.py cambiar a MYSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "josnorbel.mysql.pythonanywhere-services.com",
        "USER": "josnorbel",
        "PASSWORD": "EducacionIT2026",
        "NAME": "josnorbel$movies",
        "CHARSET": "utf8",
    }
}    