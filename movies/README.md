# Proyecto: Movies

## Aprendizaje del desarrollo de este proyecto

- Utilizando diseño HTML, responsive, esteticamente bien estructura
- Modelo de Datos acorde a la funcionalidad buscada 
- Gestión de imágenes (instalar pillow)
- Class Based View (esto agiliza la construcción de software)
- CRUDs 
- Ampliar el conocimiento del panel de Admin
- Autenticación 
- Relaciones entre modelos de datos

## Objetivo de la Aplicación

- 3 Modelos de datos
    - Género (una la película puede pertenecer a uno o mas géneros) 1 a +
    - Compañía productora (una película solo pertenece a una compañía) 1 a 1
    - Películas (definir diferentes campos de películas inclusive imagenes)

- Un usuario autenticado va a poder hacer CRUD solo sobre las películas
- Un usuario autenticado va a poder ver solamente los géneros y compañías de la aplicación    

## Tips de Desarrollo 

- Crear dos variables en settings para gestionar las imágenes
    - MEDIA_URL
    - MEDIA_ROOT
- Crear las carpetas media/movies con la misma jerarquia del proyecto    
- En el urls.py del Proyecto consultamos si estamos en modo DEBUG para utilizar una u otra variable MEDIA_[URL|ROOT]
- Super User: admin / Password: 1234

## Diseño
- Tomamos algun template existente y lo modificamos para que tome los archivos estáticos
  - img, js, css, etc.
- En la carpeta static dentro de la aplicación copiamos todas las carpetas de archivos estaticos del template

## Clase Based Views (https://ccbv.co.uk/)
- Trabaja por default con nombres por convención para los html y para los objetos que pasa a los htmls
- Por ejemplo gender_list.html, o el queryset como gender_list
- Sin embargo me permite cambiar las convenciones, podria redefinir el nombre del template (template_name)