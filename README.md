# API list_people
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

¡Bienvenido al repositorio de la API list_people! Esta API proporciona una lista de personas con un numero de cedula aleatoria para fines de experimento. Sigue esta guía para configurarla y probarla fácilmente.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración del Entorno Virtual](#configuración-del-entorno-virtual)
- [Instalación de Dependencias](#instalación-de-dependencias)
- [Ejecución de la API](#ejecución-de-la-api)
- [Pruebas con Postman](#pruebas-con-postman)
- [Puntos Finales (Endpoints)](#puntos-finales-endpoints)
- [Licencia](#licencia)

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Warp (o tu terminal preferida)
- Postman

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone [(https://github.com/Blazkull/api_personas.git)
    cd [nombre del repositorio]
    ```

## Configuración del Entorno Virtual

1.  Crea un entorno virtual usando `venv`:

    ```bash
    python -m venv venv
    ```

2.  Activa el entorno virtual:

    -   En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

    -   En Windows:

        ```bash
        venv\Scripts\activate
        ```

## Instalación de Dependencias

1.  Instala las dependencias del archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de la API

1.  Ejecuta la API:

    ```bash
    python app.py
    ```

2.  La API estará disponible en `http://localhost:[puerto]` (por defecto, el puerto suele ser 5000).

## Pruebas con Postman

1.  Abre Postman.
2.  Crea una nueva petición.
3.  Ingresa la URL del punto final que deseas probar (por ejemplo, `http://localhost:5000/usuarios`).
4.  Selecciona el método HTTP (GET).
5.  Haz clic en "Send" para enviar la petición y ver la respuesta.

## Puntos Finales (Endpoints)

Aquí tienes una lista de los puntos finales disponibles en la API:

-   `GET /usuarios`: Obtiene la lista de usuarios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
