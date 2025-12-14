from pathlib import Path

"""Configuration settings for the meal time application."""

""" Project Paths and Files Configuration """

# Project root directory. IMPORTANT: Change this to your actual project path.
project_route = Path(__file__).resolve().parent

# File to store meal times
meal_time_file = f"{project_route}/time.txt"

# File to store MD5 hashed password
password_md5_file = f"{project_route}/web/password"

# Log file for the application
log_file = f"{project_route}/logs/app.log"

""" Application Settings """

# Secret key for Flask sessions
secret_key = "iInFsb59VTorKu2a7fV2d5sPkrE7ZdXsI3wYwqFiDcdtb84hX6"

# Debug mode
debug_mode = True

# Application port
app_port = 80

# Default password
default_credentials = "admin123"

# Endpoints that do not require login
not_logged_endpoints = ('login', 'status', 'loged', 'static')

""" Hardware PI Configuration and Other Settings """

# Separator for meal times
meal_time_separator = "\n"

# GPIO PIN value for led
gpio_pin_led = 1

# GPIO PIN value for servo
gpio_pin_servo = 2