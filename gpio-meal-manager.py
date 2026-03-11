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

    servo.value = servo_min_angle

    time.sleep(dispending_time)

    servo.value = servo_max_angle

servo.value = servo_min_angle

while True:
    now = datetime.now()

    # Si cambió el día, recargamos horas y reiniciamos procesados
    if now.date() != actual_day:
        hours = get_meal_time_array()
        actual_day = now.date()
        processed_hours.clear()

    for h in hours:
        h_dt = datetime.combine(datetime.today(), h)
        
        # Ejecutar solo una vez por hora
        if h not in processed_hours and h_dt - timedelta(minutes=2) <= now <= h_dt + timedelta(minutes=2):
            dispend(h)
            processed_hours.add(h)

    time.sleep(1)
