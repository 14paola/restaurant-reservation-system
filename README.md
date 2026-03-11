# App de Reservas de Restaurante

Sistema web para la gestión de reservas de mesas en un restaurante.

La aplicación permite a los clientes consultar disponibilidad de mesas, crear reservas y cancelarlas, mientras que el administrador puede gestionar mesas y reservas desde el panel administrativo.

---

# Cómo correr el proyecto localmente

## 1 Clonar el repositorio

git clone https://github.com/tu-usuario/restaurant-reservations.git

cd restaurant-reservations


---

## 2 Crear entorno virtual

python -m venv venv

Activar entorno virtual

Windows

venv\Scripts\activate


---

## 3 Instalar dependencias

pip install -r requirements.txt


---

## 4 Ejecutar migraciones

python manage.py migrate


---

## 5 Crear superusuario

python manage.py createsuperuser


---

## 6 Ejecutar servidor

python manage.py runserver   ![Backend](images/Ejecutar servidor backend.png)

El backend quedará disponible en:

http://127.0.0.1:8000

El frontend quedará disponible en:  ![Frontend](images/Ejecutar servidor frontend.png)
http://localhost:5173 

---

# Variables de entorno

El proyecto requiere las siguientes variables de entorno.

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/reservations
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173


---

# Cómo desplegar

El sistema puede desplegarse utilizando servicios cloud como en este caso que utilice Render y Vercel. explico brevemente como lo hice yo en cada servicio cloud.

### Backend

Plataforma recomendada:

Render

Pasos básicos:

1. Crear un nuevo servicio web en Render.
2. Conectar el repositorio de GitHub.
3. Configurar las variables de entorno.
4. Ejecutar migraciones.
5. Desplegar la aplicación.

---

### Frontend

Plataforma recomendada:

Vercel

Pasos básicos:

1. Conectar el repositorio del frontend.
2. Configurar variable de entorno VITE_API_URL.
3. Desplegar la aplicación.

---

# URL de producción

Frontend

https://restaurant-reservation-system-opal.vercel.app/  

Backend API

https://restaurant-reservation-system-rzm4.onrender.com/admin/login/?next=/admin/  

---

# Usuario admin demo en Vercel (Frontend)

Para probar el panel administrativo se puede utilizar el siguiente usuario de demostración.

Usuario

paola

Password

admin123

Panel administrador:

https://restaurant-reservation-system-opal.vercel.app/admin-reservations

---

# Funcionalidades principales

- Consultar disponibilidad de mesas
- Crear reservas
- Cancelar reservas
- Panel administrativo para gestión de mesas y reservas
- Validaciones de disponibilidad y horario

---

# Testing

Ejecutar pruebas del sistema con:

python manage.py test  ![Testing](images/Pruebas test.png)

Las pruebas verifican:

- creación de reservas
- validación de disponibilidad
- reglas de negocio

---

# Documentación

La documentación incluye:

- diagrama de arquitectura  ![Diagrama1](images/Diagrama - Arquitectura.png)
- diagrama ER ![Diagrama2](images/Diagrama - ER.png)


# Capturas del sistema funcionando 

- Disponibilidad  ![Dispo](images/Pantalla principal - Disponibilidad.png)
- Reservas ![Reser](images/Pantalla principal - Reservas.png)
- Cancelación ![Cancel](images/Pantalla reserva - Cancelar.png)
- Tabla Admin ![Tabla](images/Pantalla admin - Tabla de reservas y canceladas.png)
- Filtración Admin ![Filtrar](images/Pantalla admin - Filtrada de canceladas.png)
