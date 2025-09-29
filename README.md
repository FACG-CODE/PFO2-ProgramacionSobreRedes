# PFO 2 - Programación sobre Redes

**Alumno:** Francisco Agustín Cruz Guantay

---

## 📖 Descripción

Este proyecto implementa un **sistema de gestión de usuarios con autenticación** y una pequeña API web en Flask.
Permite registrar usuarios, iniciar sesión desde la consola y, tras la autenticación, abrir un navegador mostrando un HTML de bienvenida.

---

## 📂 Estructura del repositorio

```
PFO2-PROGRAMACIONSOBREREDES/
│
├── 📂 pruebas/
│   └── 📂 capturas/              # Evidencias gráficas de funcionamiento
│       ├── Campos incompletos.png
│       ├── Error al iniciar sesion.png
│       ├── Inicio de sesion exitoso.png
│       ├── Registro de nuevo usuario.png
│       ├── Renderizado de HTML.png
│       └── Usuario ya existe en la DB.png
│
├── 📂 src/
│   ├── 📂 templates/             # Plantilla HTML renderizada por Flask
│   │   └── bienvenida.html    
│   ├── persistencia.db           # Archivo DB generado automaticamente por SQLite
│   └── servidor.py               # Script principal (servidor Flask y configuración de la DB)
│    
├── ⚡ ejecutar_servidor.bat       # Script de ejecución automatizada
│
└── 📝 README.md                   # Documentación del proyecto
```

## 📝 Se cubren los objetivos del PFO 2:

1. Implementar una API REST con endpoints funcionales.
2. Usar autenticación con protección de contraseñas (hash).
3. Gestionar datos persistentes con SQLite.
4. Construir un cliente en consola que interactúe con la API.
5. 📸 Capturas de pruebas de funcionamiento realizadas en carpeta `pruebas/capturas`.
6. ⚠️ El repositorio solamente se encuentra subido a GitHub, **no se utiliza GitHub Pages** ya que este solo admite sitios estáticos, mientras que en este caso se trata de una aplicación dinámica con servidor Flask que requiere ejecución en un entorno de servidor.

---

## 🔑 Funcionalidades

1. Registro de usuarios

   Almacena usuarios en SQLite.
   Las contraseñas se guardan hasheadas usando werkzeug.security.
   Endpoint (simulado desde consola): POST /registro.

2. Inicio de sesión

   Verifica credenciales de usuario desde SQLite.
   Al iniciar sesión correctamente, se levanta un servidor Flask y se abre un navegador con un HTML de bienvenida.
   Endpoint (simulado desde consola): POST /login.

## 🛠️ Requisitos técnicos
   Python 3.x
   Librerías externas:
   flask → para servidor web y renderizado HTML.
   werkzeug → para hashear y verificar contraseñas de manera segura.
   Persistencia de datos: SQLite (persistencia.db).
   Archivo principal: servidor.py.

## 🚀 Instalación y ejecución
   Ejecutar el archivo .bat incluido (ejecutar_servidor.bat) que:
   Instala automáticamente flask y werkzeug si no están presentes.
   Ejecuta el script servidor.py.

   ## Opcional (manual):

   1. Clonar el repositorio o descargar el proyecto.
   2. Abrir la terminal en la carpeta src del proyecto.
   3. Instalar librerías externas: `pip install flask werkzeug`
   4. Para correr el programa en consola ejecutar en el terminal: `python servidor.py`

## 📝 Respuestas conceptuales

   1. ¿Por qué hashear contraseñas?
   Protege la seguridad del usuario, evita que las contraseñas se guarden en texto plano, e incluso si alguien accede a la base de datos, no podrá ver las contraseñas reales.

   2. Ventajas de usar SQLite en este proyecto
   Ligero y fácil de configurar, no requiere servidor adicional (se guarda todo localmente). Es compatible con Python y permite consultas SQL simples para registro y autenticación.
