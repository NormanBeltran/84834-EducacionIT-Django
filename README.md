Prof. Norman Beltran

Django 

Documentación a seguir

# Primera vez

En una carpeta vacia de nuestro disco:

- Crear el environment python -m venv env
- Ejecutar env\Scripts\ctivate (ctivar el environmennt)
- Instalar Django ejecutando pip install django
- django-admin startproject mip 
- Ingresar a la carpeta del proyecto con cd mip
- django-admin startapp miapp

# Luego en desarrollo

- Seteamos las variables y configuraciones dentro de la carpeta del proyecto
- Modificando settings.py:
    - Agregar la app dentro de INSTALLED_APPS
    - Opcional cambiar las variables de LANGUAGE, TIME

- En urls.py
    - Definimos derivar todas las rutas que correspondan a la aplicación al urls.py de la carpeta de la aplicacion
    - views.py vamos definiendo las funciones que van a resolver cada petición

# DTL
- Variables {{ }}
- Estructuras {% if ... %} {% for ... %}
- {% url 'name' %} que esta definido en urls.py

# Parametros por la URL

- En la funcion se ponen todos los parametros esperados
- En urls.py se agrega a la ruta al final los parametros que se convertiran en los arguemntos recibidos por la función

# Formularios

- Crear forms.py en la carpeta de la aplicacion
- Crear una clase con todos los campos heredando de forms.Form
- Para cada campo utilizar las opciones de forms.CharField 
- Importar en views el forms
- En base al flujo analizar si es la primera o enesima vez
    - Crear un form vacio (si es la primera vez)
    - Popular con request.POST si es la enesima vez
    - Validar que el formulario tenga los datos válidos
    - Si todo es válido ejecutar la acción (p.e. guardar los datos en la BD)
    - retornar a la pagina elegida