# 🚗 JMAutomovil - Sistema de Venta de Automóviles / Car Sales System

## 🇪🇸 Español

Este repositorio contiene el código fuente de **JMAutomovil**, un sistema de **venta de automóviles** desarrollado con **Django**. La plataforma permite gestionar vehículos de manera eficiente, permitiendo **agregar, modificar y eliminar automóviles** a través de una interfaz protegida con autenticación.

### 🛠 Tecnologías Utilizadas

- 🐍 **Django 5.0.7** → Framework web principal
- 🗄️ **Base de datos SQLite** → Almacenamiento y gestión de información
- 🎨 **Bootstrap** → Diseño responsivo y moderno
- 💾 **CSS y JavaScript estáticos** → Personalización de la interfaz
- 🔐 **Sistema de Login** → Acceso a la interfaz de administración de vehículos

### 🎯 Objetivo del Proyecto

El objetivo de **JMAutomovil** es permitir la **gestión sencilla de vehículos** en una plataforma web. Los automóviles registrados en la base de datos se **añaden automáticamente** a la web para su visualización, ofreciendo una experiencia fluida y automatizada.

### 🗃️ Estructura de la Base de Datos

**Django ORM** fue utilizado para modelar la base de datos, definiendo las siguientes entidades:

- **Vehículo**:
  - `marca`: Marca del vehículo
  - `modelo`: Modelo del automóvil
  - `año`: Año del modelo
  - `cilindrada`: Capacidad del motor
  - `tipo_combustible`: Tipo de combustible (gasolina, diésel, eléctrico, etc.)
  - `transmisión`: Tipo de transmisión (manual o automática)

- **Usuario**:
  - `nombre_usuario`: Nombre de usuario único
  - `email`: Correo electrónico
  - `contraseña`: Almacenada de forma segura
  - `es_admin`: Indica si el usuario tiene privilegios de administrador

Solo los usuarios autenticados pueden **agregar, modificar o eliminar vehículos**.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## En English

This repository contains the source code for **JMAutomovil**, a **car sales system** developed with **Django**. The platform allows efficient vehicle management, enabling **adding, modifying, and deleting cars** through an authentication-protected interface.

### 🛠 Technologies Used

- 🐍 **Django 5.0.7** → Main web framework
- 🗄️ **SQLite Database** → Data storage and management
- 🎨 **Bootstrap** → Responsive and modern design
- 💾 **Static CSS and JavaScript** → UI customization
- 🔐 **Login System** → Access control for vehicle management

### 🎯 Project Objective

The goal of **JMAutomovil** is to facilitate **simple vehicle management** on a web platform. Vehicles registered in the database are **automatically added** to the website for display, ensuring a seamless and automated experience.

### 🗃️ Database Structure

**Django ORM** was used to model the database, defining the following entities:

- **Vehicle**:
  - `brand`: Vehicle brand
  - `model`: Car model
  - `year`: Model year
  - `engine_capacity`: Engine capacity
  - `fuel_type`: Type of fuel used (gasoline, diesel, electric, etc.)
  - `transmission`: Transmission type (manual or automatic)

- **User**:
  - `username`: Unique username
  - `email`: User's email address
  - `password`: Securely stored with hashing
  - `is_admin`: Indicates whether the user has admin privileges

Only authenticated users can **add, modify, or delete vehicles**.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Estado del Proyecto / Project Status

✅ **Proyecto Completado** y listo para su uso. Futuras mejoras pueden implementarse para optimizar la experiencia del usuario.

✅ **Project Completed** and ready for use. Future improvements may be implemented to optimize the user experience.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📄 Licencia / License

Este proyecto está en constante mejora. ¡Si deseas contribuir o sugerir cambios, eres bienvenido! 🚀

This project is constantly evolving. If you wish to contribute or suggest changes, you are welcome! 🚀
