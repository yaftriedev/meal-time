# Meal-Time

**Meal-Time** is a software solution that allows you to **manage your pets' feeding through a web interface**, remotely controlling a physical system (indicator light and servo motor) and configuring feeding schedules in a simple and secure way.

---

## 🚀 Features

* Web interface to manage feeding schedules
* Password-based authentication
* Password change directly from the web UI
* Hardware control (light and servo)
* Session-based route protection
* Minimal status endpoint for monitoring

---

## 🛠️ Instalation

* **Using docker**: ```docker build -t meal-time```.
* **Normal Installing**: ``` pip install -r requirements.txt ```.
* **Installing with venv**: 
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Instaling Ngrok

* **Download from repo**: 
    * ``` wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.zip ```
    * ``` wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.zip ```
    * ``` wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip ```
* **Unzip and Install**: ```unzip ngrok-*.zip``` ```sudo mv ngrok /usr/local/bin/```
* **Configure the Token**: ```ngrok config add-authtoken TOKEN```
* **Start the Server**: ```ngrok http 5000```

## 🔌 Hardware

The system is designed to run on a microcontroller or single-board computer (for example, a Raspberry Pi).

* **Light pin**: `1`
* **Servo pin**: `2`

> ⚠️ Update these values in the code according to your actual hardware setup.

---

## 🌐 Web architecture

The web application is built using **Flask** and relies on sessions to control access to protected routes.

### Authentication middleware

Before every request, the application checks whether the user is authenticated:

```python
@app.before_request
def check_login():
    if request.endpoint not in not_logged_endpoints and not session.get('logged_in', False):
        return redirect(url_for('login'))
```

Routes accessible without authentication:

* `login`
* `status`
* `loged`
* `static`

---

## 📍 Available routes

### `/` — Main page

**Methods**: `GET`, `POST`

Responsibilities:

* Render the main interface
* Change the application password
* Configure feeding times

Possible `POST` actions:

* **Password change**

  * Validates that the password is not empty
  * Prevents reusing the previous password
  * Stores the password with bcrypt

* **Feeding schedule update**

  * Validates the time format
  * Saves feeding times to a file

---

### `/login` — Login

**Methods**: `GET`, `POST`

* Displays the login form
* Verifies the password using bcrypt
* Starts a user session (`logged_in = True`)

---

### `/logout` — Logout

**Methods**: `GET`, `POST`

* Ends the current session
* Redirects the user to the login page

---

### `/status` — Service status

**Method**: `GET`

* Returns:

```
OK
```

Useful for:

* Health checks
* Monitoring
* External scripts

---

### `/loged` — Authentication status

**Method**: `GET`

* Returns:

  * `True` if the user is authenticated
  * `False` otherwise

---

## 🔐 Security

* Session-based authentication
* Passwords stored with bcrypt

---

## 📦 Requirements

* Python 3
* Flask
* GPIO-compatible hardware
* Bcrypt

---

## 📄 License

Personal / educational project. Use at your own risk.
