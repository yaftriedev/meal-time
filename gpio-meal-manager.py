import time
from web.util import get_meal_time_array
from datetime import datetime
from gpiozero import LED, Servo
from config import gpio_pin_led, gpio_pin_servo, dispending_time, aditional_led_time, log_file

led = LED(gpio_pin_led)
servo = Servo(gpio_pin_servo)

hours = get_meal_time_array()
actual_day = datetime.now().date()

# Function to dispend
def dispend(h):
    with open(log_file, "w") as l:
        l.write(f"Dispensing meal at {h} on {datetime.now()}\n")

    servo.max()
    led.on()

    time.sleep(dispending_time)

    servo.min()

    time.sleep(aditional_led_time)

    lod.off()

# min -> closed
# max -> open
servo.min()

for i in range(1, 5):
    led.toggle()
    time.sleep(1)

led.off()

while True:
    now = datetime.now()

    # If day has changed, reload hours
    if now.date() != actual_day:
        hours = get_meal_time_array
        dia_actual = now.date()

    # Schedule meals
    scheduled_hours = [h for h in hours if 
                       (now.hour, now.minute, now.second) >= (h.hour, h.minute, h.second)]

    for h in scheduled_hours:
        dispend(h)
        hours.remove(h)

    time.sleep(1)
