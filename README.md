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

# HTML Diseño Bootstrap https://getbootstrap.com    

## Diseño
- Crear un archivo base.html / index.html que va a contener todo el diseño de la aplicación
- Crear los bloques que van a ir cambiando a lo largo de la navegación
- Leer los archivos estáticos que tienen que estar en la carpeta:
    - static (dentro de la aplicación), pueden ser archivos css, javascript, imagenes, videos, audios

- Para heredar el diseño, cualquier pagina que se cree, tiene que extender el base.html
- Y cada bloque se redefina tiene que estar encerrado entre {% block nombre %}contenido{% endblock %}

# ORM (Object Relational Mapping)
- En models.py dentro de la carpeta de la aplicacion creamos las clases que van a formar parte de las 
tablas de mi BD
- Ejecutamos desde la terminal python manage.py makemigrations [miapp]
  - Esto crea los scripts para despues crear las tablas en la BD
- Ejecutamos desde la terminal python manage.py migrate
  - Ejecuta los scripts para crear las tablas en la BD

# Formularios con ORM
- en forms.py:
    - importamos ModelForm (este modulo vincula Form con Model)
    - La clase formulario la heredamos de ModelForm
    - Creamos una clase Meta (metadatos) donde definimos el model y fields con los campos que queremos
    que aparezcan en el formulario
- En views.py en la funcion directamente grabamos el form (porque esta asociado a el modelo con todos sus atributos)

# Ejemplos de instrucciones ORM de Django https://unwiredlearning.com/blog/django-orm-crud

# Aplicacion Admin que viene por default con Django

## Objetivo
   - Permite administrar autenticación y autorización en el panel de administracion
   - Gestiona permisos a nivel de usuario o grupos
   - Grupos son roles donde agrupo los permisos sobre los modelos a nivel de 
     - visualizacion
     - actualizacion
     - creacion de registros
     - eliminacion de registros

## Como gestionar modelos en el panel     
- Crear el superuser: python manage.py createsuperuser
- Para incorporar modelos de negocio:
    - abrir el admin.py dentro de la aplicacion
    - importar clases de modelos con: from .models import * 
    - registrar los modelos con admin.site.register(nombre_modelo)

## Caracteristicas especiales
- Podemos gestionar nombres de los modelos en plural o singular en la clase Meta dentro de la 
  clase del modelo
- También podemos definir el orden de presentación con el campo ordering

## Look & Feel de Panel de Admin
- https://django-jazzmin.readthedocs.io/

