# Sistema de Gestión de Catequesis

Sistema web desarrollado en Django para la administración de alumnos de catequesis, con funcionalidad CRUD completa y conexión a base de datos SQL Server.

## 🚀 Características

- ✅ **CRUD completo** de alumnos (Crear, Leer, Actualizar, Eliminar)
- 🎨 **Interfaz moderna** con Tailwind CSS
- 🔒 **Gestión segura** de credenciales con archivos de configuración
- 💾 **Conexión a SQL Server** con soporte para bases de datos existentes
- 📱 **Diseño responsivo** adaptable a dispositivos móviles

## 📋 Requisitos Previos

- Python 3.8 o superior
- SQL Server (local o remoto)
- ODBC Driver 17 for SQL Server

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/galeyro/P2-S7-Fase-4-Proyecto-Integrador.git
cd P2-S7-Fase-4-Proyecto-Integrador
```

### 2. Crear y activar un entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django mssql-django pyodbc
```

### 4. Configurar la base de datos

1. Copia el archivo de ejemplo:

   ```bash
   cp config.json.example config.json
   ```

2. Edita `config.json` con tus credenciales:
   ```json
   {
     "database": {
       "ENGINE": "mssql",
       "NAME": "TU_BASE_DE_DATOS",
       "USER": "tu_usuario",
       "PASSWORD": "tu_contraseña",
       "HOST": "localhost",
       "PORT": "1433",
       "OPTIONS": {
         "driver": "ODBC Driver 17 for SQL Server",
         "unicode_results": true
       }
     }
   }
   ```

### 5. Estructura de la tabla Alumno

El sistema espera que exista una tabla `Alumno` con la siguiente estructura:

```sql
CREATE TABLE Alumno (
    id_alumno INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    apellido NVARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NULL,
    lugar_nacimiento NVARCHAR(100) NULL,
    direccion NVARCHAR(255) NULL,
    telefono_alumno NVARCHAR(20) NULL,
    info_escolar NVARCHAR(255) NULL,
    info_salud NVARCHAR(500) NULL
);
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000/**

## 📁 Estructura del Proyecto

```
P2-S7-Fase-4-Proyecto-Integrador/
│
├── catequesis/              # Configuración del proyecto Django
│   ├── settings.py          # Configuración principal
│   ├── urls.py              # URLs principales
│   └── templates/           # Templates globales
│       └── index.html       # Interfaz CRUD
│
├── catequesis_app/          # Aplicación principal
│   ├── models.py            # Modelo Alumno
│   ├── views.py             # Vistas CRUD
│   └── urls.py              # URLs de la app
│
├── config.json              # Credenciales DB (no se sube a Git)
├── config.json.example      # Plantilla de configuración
├── manage.py                # Script de gestión Django
└── README.md                # Este archivo
```

## 🔐 Seguridad

- El archivo `config.json` con las credenciales está incluido en `.gitignore`
- **Nunca subas** tu `config.json` al repositorio
- Usa `config.json.example` como referencia para la configuración

## 🎯 Funcionalidades

### Crear Alumno

Completa el formulario con los datos del alumno y haz clic en "Guardar".

### Listar Alumnos

La tabla muestra todos los alumnos registrados con sus datos principales.

### Editar Alumno

Haz clic en "Editar" en la fila del alumno. El formulario se llenará automáticamente con sus datos.

### Eliminar Alumno

Haz clic en "Eliminar" y confirma la acción. Esta operación no se puede deshacer.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django 5.2.8
- **Base de datos:** Microsoft SQL Server
- **Frontend:** HTML5, JavaScript (Vanilla), Tailwind CSS
- **ORM:** Django ORM con mssql-django
- **Driver:** pyodbc + ODBC Driver 17 for SQL Server

## 📝 Notas Importantes

- El modelo usa `managed = False`, por lo que Django no creará ni modificará la tabla
- No es necesario ejecutar `python manage.py migrate` si solo usas tu tabla existente
- Si necesitas usar el admin de Django o autenticación, ejecuta las migraciones


## 👤 Autores

**Arias Javier, Andrade Eduardo y Galo Guevara**

- GitHub: [@galeyro](https://github.com/galeyro)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).

---

⭐ Si te ha sido útil este proyecto, considera darle una estrella en GitHub!
