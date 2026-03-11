# Restaurant Reservation System - Backend

Backend desarrollado con Django, Django REST Framework y PostgreSQL para la gestión de reservas de restaurante.

## Tecnologías usadas

- Python 3.12
- Django 6
- Django REST Framework
- PostgreSQL
- Simple JWT
- CORS Headers

## Funcionalidades implementadas

- Gestión de mesas
- Gestión de configuración del restaurante
- Consulta de disponibilidad
- Creación de reservas con asignación automática de mesa
- Cancelación de reservas por código
- Listado de reservas para administrador
- Autenticación JWT
- Pruebas básicas

## Estructura del proyecto

- `tables`: gestión de mesas
- `reservations`: lógica de reservas
- `restaurant_settings`: configuración del restaurante
- `accounts`: autenticación con JWT

## Requisitos previos

Antes de ejecutar el proyecto, debe estar instalado:

- Python 3.12
- PostgreSQL
- Visual Studio Code
- Thunder Client o Postman para probar endpoints

## Configuración del entorno

Crear un archivo `.env` en la raíz de `backend` con el siguiente contenido:

```env
SECRET_KEY=django-insecure-cambia-esto
DEBUG=True
DB_NAME=restaurant_db
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432