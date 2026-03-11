import time
from web.util import get_meal_time_array
from datetime import datetime
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

    update_hours = get_meal_time_array()
    for h in updated_hours:
        if h not in hours and (h.hour, h.minute, h.second) > (now.hour, now.minute, now.second) :
            hours.append(h)

    # Schedule meals
    scheduled_hours = [h for h in hours if 
                       (now.hour, now.minute, now.second) >= (h.hour, h.minute, h.second)]

    for h in scheduled_hours:
        dispend(h)
        hours.remove(h)

    time.sleep(1)
