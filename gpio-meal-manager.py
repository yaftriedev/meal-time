import time
from web.util import get_meal_time_array
from datetime import datetime
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from config import *

factory = PiGPIOFactory()
servo = Servo(gpio_pin_servo, pin_factory=factory)

hours = get_meal_time_array()
actual_day = datetime.now().date()

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

    # If day has changed, reload hours
    if now.date() != actual_day:
        hours = get_meal_time_array()
        actual_day = now.date()

    updated_hours = get_meal_time_array()
    for h in updated_hours:
        if h not in hours and if h - timedelta(minutes=2) <= now <= h + timedelta(minutes=2):
            hours.append(h)

    # Schedule meals
    scheduled_hours = [h for h in hours if h - timedelta(hours=1) <= now <= h + timedelta(hours=1)]

    for h in scheduled_hours:
        dispend(h)
        hours.remove(h)

    time.sleep(1)
