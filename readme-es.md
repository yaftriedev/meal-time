# Meal-Time

**Meal-Time** es un software que permite **gestionar la comida de tus mascotas a través de una interfaz web**, controlando de forma remota un sistema físico (luz indicadora y servo) y configurando horarios de comida de manera sencilla y segura.

---

## 🚀 Funcionalidades

* Interfaz web para gestión de horarios de comida
* Autenticación mediante contraseña
* Cambio de contraseña desde la web
* Control de hardware (luz y servo)
* Sistema de sesiones para proteger rutas
* API mínima de estado para monitorización

---

## 🔌 Hardware

El sistema está pensado para funcionar con un microcontrolador (por ejemplo, Raspberry Pi o similar).

* **Pin de la luz**: `1`
* **Pin del servo**: `2`

> ⚠️ Ajusta estos valores en el código según el hardware real utilizado.

---

## 🌐 Arquitectura web

La aplicación web está construida con **Flask** y utiliza sesiones para controlar el acceso a las rutas.

### Middleware de autenticación

Antes de cada petición, se comprueba si el usuario está autenticado:

```python
@app.before_request
def check_login():
    if request.endpoint not in not_logged_endpoints and not session.get('logged_in', False):
        return redirect(url_for('login'))
```

Las rutas accesibles sin login son:

* `login`
* `status`
* `loged`
* `static`

---

## 📍 Rutas disponibles

### `/` — Página principal

**Métodos**: `GET`, `POST`

Funcionalidades:

* Mostrar la interfaz principal
* Cambiar la contraseña
* Configurar los horarios de comida

Acciones posibles vía `POST`:

* **Cambio de contraseña**

  * Valida que no esté vacía
  * Evita reutilizar la contraseña anterior
  * Se almacena en formato MD5

* **Actualización de horarios de comida**

  * Valida el formato del tiempo
  * Guarda los horarios en archivo

---

### `/login` — Inicio de sesión

**Métodos**: `GET`, `POST`

* Muestra el formulario de login
* Verifica la contraseña usando hash MD5
* Inicia la sesión (`logged_in = True`)

---

### `/logout` — Cierre de sesión

**Métodos**: `GET`, `POST`

* Cierra la sesión del usuario
* Redirige a la página de login

---

### `/status` — Estado del servicio

**Método**: `GET`

* Devuelve simplemente:

```
OK
```

Útil para:

* Health checks
* Monitorización
* Scripts externos

---

### `/loged` — Estado de autenticación

**Método**: `GET`

* Devuelve:

  * `True` si el usuario está autenticado
  * `False` en caso contrario

---

## 🔐 Seguridad

* Autenticación basada en sesiones
* Contraseñas almacenadas como hash MD5


---

## 📦 Requisitos

* Python 3
* Flask
* Hardware compatible con control de GPIO

---

## 📄 Licencia

Proyecto educativo / personal. Uso libre bajo tu propia responsabilidad.
