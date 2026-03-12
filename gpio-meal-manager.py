import time
from web.util import get_meal_time_array
from datetime import datetime, timedelta
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from config import *

factory = PiGPIOFactory()
servo = Servo(gpio_pin_servo, pin_factory=factory)

hours = get_meal_time_array()
actual_day = datetime.now().date()
processed_hours = set()

# Function to dispend
def dispend(h):
    with open(log_file, "a") as l:
        l.write(f"Dispensing meal at {h} on {datetime.now()}\n")

    servo.value = servo_max_angle
    time.sleep(dispending_time)
    servo.value = servo_min_angle

servo.value = servo_min_angle

def check_and_dispense(h_list, now, margin_minutes=2, catchup_hours=1):
    """
    Ejecuta las comidas dentro de ±margin_minutes de ahora,
    y también las que hayan pasado hasta catchup_hours atrás (solo al inicio)
    """
    for h in h_list:
        h_dt = datetime.combine(datetime.today(), h)

        # Si no se ha procesado
        if h not in processed_hours:
            # Rango normal ±margin_minutes
            if h_dt - timedelta(minutes=margin_minutes) <= now <= h_dt + timedelta(minutes=margin_minutes):
                dispend(h)
                processed_hours.add(h)
            # Catchup: comidas que pasaron hasta catchup_hours atrás
            elif now - timedelta(hours=catchup_hours) <= h_dt < now - timedelta(minutes=margin_minutes):
                dispend(h)
                processed_hours.add(h)

# Ejecutamos catchup al inicio
now = datetime.now()
check_and_dispense(hours, now, margin_minutes=2, catchup_hours=1)

while True:
    now = datetime.now()

    # Si cambió el día, recargamos horas y reiniciamos procesados
    if now.date() != actual_day:
        hours = get_meal_time_array()
        actual_day = now.date()
        processed_hours.clear()

    check_and_dispense(hours, now, margin_minutes=2, catchup_hours=0)  # catchup=0 durante ejecución normal

    time.sleep(1)
