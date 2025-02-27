# 🚗 JMAutomovil - Sistema de Venta de Automóviles

Este repositorio contiene el código fuente de **JMAutomovil**, un sistema de **venta de automóviles** desarrollado con **Django**. La plataforma permite gestionar vehículos de manera eficiente, permitiendo **agregar, modificar y eliminar automóviles** a través de una interfaz protegida con autenticación.

---

## 🛠 Tecnologías Utilizadas

- 🐍 **Django 5.0.7** → Framework web principal
- 🗄️ **Base de datos SQLite** → Almacenamiento y gestión de información
- 🎨 **Bootstrap** → Diseño responsivo y moderno
- 💾 **CSS y JavaScript estáticos** → Personalización de la interfaz
- 🔐 **Sistema de Login** → Acceso a la interfaz de administración de vehículos

---

## 🎯 Objetivo del Proyecto

El objetivo de **JMAutomovil** es permitir la **gestión sencilla de vehículos** en una plataforma web. Los automóviles registrados en la base de datos se **añaden automáticamente** a la web para su visualización, ofreciendo una experiencia fluida y automatizada.

---

## 🗃️ Estructura de la Base de Datos

Se utilizó **Django ORM** para modelar la base de datos, definiendo las siguientes entidades:

- **Vehículo**: Representa un automóvil en el sistema con los siguientes campos:
  - `marca`: Marca del vehículo
  - `modelo`: Modelo del automóvil
  - `año`: Año del modelo
  - `cilindrada`: Capacidad del motor
  - `tipo_combustible`: Tipo de combustible utilizado (gasolina, diésel, eléctrico, etc.)
  - `transmisión`: Tipo de transmisión (manual o automática)
  
- **Usuario**: Gestión de usuarios con autenticación para acceder a la administración del sistema:
  - `nombre_usuario`: Nombre de usuario único
  - `email`: Correo electrónico del usuario
  - `contraseña`: Almacenada de forma segura con hash
  - `es_admin`: Indica si el usuario tiene permisos de administrador

Cada vehículo ingresado en el sistema se guarda en la base de datos y se muestra automáticamente en la web. Solo los usuarios con privilegios de admin pueden **agregar, modificar o eliminar vehículos**.

---

## ✨ Características Principales

- ✅ **Gestión completa de vehículos** (marca, modelo, año, cilindrada, tipo de combustible, transmisión)
- ✅ **Interfaz protegida con Login** para administración
- ✅ **Sistema de usuarios con autenticación y permisos**
- ✅ **Añadir, modificar y eliminar vehículos** fácilmente
- ✅ **Carga automática de nuevos vehículos en la web**
- ✅ **Diseño responsivo y atractivo con Bootstrap**
- ✅ **Modelado de base de datos con Django ORM**, con creación y gestión de tablas automáticamente

---

## 📌 Estado del Proyecto

✅ **Proyecto Completado** y listo para su uso. Futuras mejoras pueden implementarse para optimizar la experiencia del usuario.

---

## 📄 Licencia

Este proyecto está en constante mejora. ¡Si deseas contribuir o sugerir cambios, eres bienvenido! 🚀
