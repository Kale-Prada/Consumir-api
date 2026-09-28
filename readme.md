# Aprendiendo a consumir API

**Aplicación de Python para consumir API con request.**


- El cliente (mi programa): Envía una petición (request) a través de una dirección web o URL (endpoints).
- El intermediario (la API): Recibe la petición, sigue un conjunto de reglas y se comunica con el servidor.
- El servidor: Procesa la información y devuelve una respuesta en formato JSON.

## Detalles de este ejercicio:

La API accede a los datos contenidos en el endpoint https://api.chucknorris.io/jokes/categories devuelve una lista en formato JSON con todas las categorías disponibles que se pueden usar para filtrar chistes de Chuck Norris. 

- Método HTTP: GET
- Autenticación: No requiere clave ni registro.
- Formato de respuesta: Un array JSON con cadenas de texto (strings) que representan los nombres de las categorías válidas.


## Detalles para ejecutar la API en tu entorno


### Instalación y Ejecución

1. Clona o descarga el repositorio en tu equipo.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Crea y activa un entorno virtual:
    ```bash
    # Para crear el entorno: 
    # En Windows: 
    python -m venv entorno
    
    #Otra opción: 
    py -m venv entorno 

    # En MacOS: 
    python3 -m venv entorno

    # Para activar el entorno: 
    # En Windows (PowerShell):
    .\entorno\Scripts\activate

    # En macOS/Linux:
    source entorno/bin/activate
    ```
    _Tu entorno estará activo cuando veas el nombre (entorno) al principio de la línea de comandos de tu terminal._
   
4. Instala las librerías necesarias ejecutando:
   ```bash
   # En Windows:
   pip install -r requirements.txt

   # En macOS/Linux:
   pip3 install -r requirements.txt
   ```

## Requerimientos
Instala requirements.txt / Ten en cuenta estas librerías: 


## Licencia

Autor = Keepcoding España S.L.U. 

## Acerca de Chuck Norris IO: 

**Ver en Github:**  [Chuck Norris IO](https://github.com/chucknorris-io) 

**Ver Web:** [Chuck Norris](https://api.chucknorris.io/)


