# User Management System

Este proyecto es un sistema de gestión de usuarios desarrollado con Django y MySQL. Incluye características como la creación y edición de usuarios, así como una interfaz para usuarios estándar y administradores.

## Requisitos Previos

Asegúrate de tener instalado Python 3.11 y Django 4.2.4 antes de comenzar.

install python==3.11
install django==4.2.4

## Instalación

**Instala las dependencias necesarias:**
1. pip install mysqlclient
2. pip install reportlab
3. pip install djangorestframework

**Realiza las migraciones para configurar la base de datos:**
1. python manage.py migrate

**Crea un superusuario para acceder a la interfaz administrativa:**
1. python manage.py createsuperuser
Sigue las instrucciones en la consola para proporcionar el nombre de usuario, correo electrónico y contraseña del superusuario.

## Ejecución
python manage.py runserver

## Interfaz Administrativa

Accede a la interfaz administrativa en http://127.0.0.1:8000/admin/ con las credenciales del superusuario.

Recuerda adaptar la información según las necesidades específicas de tu proyecto.


[Ver Video en Facebook](https://www.facebook.com/100005895122733/videos/377829711415156/)
